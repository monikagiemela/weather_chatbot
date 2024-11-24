import os
import json
import requests
from app.sys_config import system_instruction


OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GPT_MODEL = "gpt-4o-mini"

messages = [
    {"role": "system", "content": system_instruction}
]

functions = [
    {
        "name": "handle_weather_query",
        "description": "Parse user query for weather information, determine if it's for current or future weather, and call the weather API with the user measag and appropriate location parameters.",
        "parameters": {
            "type": "object",
            "properties": {
                "user_message": {
                    "type": "string",
                    "description": "The user's message asking for weather information, e.g., 'What's the weather in New York tomorrow?'",
                },
                "location": {
                    "type": "string",
                    "description": "The city and state for the weather request, e.g., 'San Francisco, CA'.",
                }
            },
            "required": ["user_message", "location"],
        },
    }
]


def chat_completion_request(messages, functions=None, function_call=None, model=GPT_MODEL):
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + OPENAI_API_KEY,
    }
    json_data = {
        "model": model, 
        "messages": messages
    }
    if functions is not None:
        json_data.update({"functions": functions})
    if function_call is not None:
        json_data.update({"function_call": function_call})

    try:
        print(f"\n>>>> JSON Data to be sent: {json.dumps(json_data, indent=2)}")
        response = requests.post(
            "https://api.openai.com/v1/chat/completions",
            headers=headers,
            json=json_data,
        )

        if response.status_code != 200:
            print(f"\n>>>> Error response from API: {response.status_code}, {response.text}")

        return response
    except Exception as e:
        print(f"\n>>>> Unable to generate ChatCompletion response")
        print(f"\n>>>> Exception: {e}")
        raise e

