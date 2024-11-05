import openai
from dotenv import load_dotenv
import chainlit as cl
from src.llm import chat_completion_request, messages, functions
from src.sys_config import conv_prompt
from src.utils import handle_weather_query
import json
import os

load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

import json

def execute_function_call(assistant_message):
    try:
        if assistant_message.get("function_call", {}).get("name") == "handle_weather_query":
            arguments = json.loads(assistant_message["function_call"]["arguments"])
            location = arguments["location"]
            user_message = arguments['user_message']
            results = handle_weather_query(location=location, user_message=user_message)
        else:
            results = f"Error: function {assistant_message['function_call']['name']} does not exist"
    except Exception as e:
        results = f"Function call execution failed: {str(e)}"
        print(f"\n>>>> Error executing function call: {results}")

    print(f"\n>>>> Results obtained from executing function call: \n{results}\n")
    return results



def get_natural_response(content, user_message):
    convert_prompt = conv_prompt.replace("<query>", user_message.content).replace("<api_result>", content)
    messages.append({"role": "user", "content": convert_prompt})
    convert_prompt_response = chat_completion_request(messages=messages)
    print(f"\n>>>> received message: {convert_prompt_response.json()}")
    new_assistant_message = convert_prompt_response.json()["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": new_assistant_message})
    print(f"\n>>>> natural response: \n{new_assistant_message}")
    return new_assistant_message

# Main function
@cl.on_message
async def main(message: cl.message.Message):
    # Add user message content to conversation history
    messages.append({"role": "user", "content": message.content})
    print(f"\n>>>> user message: {messages}")
    
    # Make API request
    chat_response = chat_completion_request(messages=messages, functions=functions)
    print(f"\n>>>> complete_chat_response: \n{chat_response.json()}\n")
    
    assistant_message = chat_response.json()["choices"][0]["message"]
    print(f"\n>>>> assistant message: \n{assistant_message}\n")

    # Check if there's a function call
    if assistant_message.get("function_call"):
        results = execute_function_call(assistant_message)
        content = get_natural_response(json.dumps(results), message)
    else:
        # Handle simple response from assistant
        content = assistant_message["content"]
        messages.append({"role": "assistant", "content": content})
        print(f"\n>>>> results obtained: \n{content}\n")
    
    print(f"\n>>>> Chat response: {content}\n")

    # Send response through Chainlit
    await cl.Message(content=content).send()


