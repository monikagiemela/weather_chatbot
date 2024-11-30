# Weather Chatbot  

This project is a weather chatbot designed to provide real-time weather information like temperature, wind speed, precipitation, and weather conditions. The chatbot uses **OpenAI’s GPT-4o-mini model** with **prompt engineering**, **chat completions**, and **function calling** to deliver accurate and conversational weather forecasts by integrating with the **WeatherAPI** via **RapidAPI**.  

---

## **Features**  
- Real-time weather updates using live data from **WeatherAPI**.  
- Conversational interface powered by **GPT-4o-mini**.  
- User-friendly responses formatted for clarity and precision.  

---

## **Technologies Used**  

| **Technology**       | **Purpose**                                                                                               | **Link**                                                                                 |  
|-----------------------|-----------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|  
| OpenAI GPT-4o-mini    | Natural language understanding and response generation.                                                  | [OpenAI GPT-4o-mini](https://platform.openai.com/docs/models#gpt-4o-mini)               |  
| Chat Completions      | Conversational response generation.                                                                      | [Chat Completions](https://platform.openai.com/docs/api-reference/chat/create)          |  
| Prompt Engineering    | To guide and optimize GPT responses.                                                                     | [Prompt Engineering](https://platform.openai.com/docs/guides/prompt-engineering)        |  
| Function Calling      | To retrieve live data by interacting with APIs.                                                          | [Function Calling](https://platform.openai.com/docs/guides/function-calling)            |  
| WeatherAPI (via RapidAPI) | To fetch live weather information such as temperature, wind speed, and precipitation.                 | [WeatherAPI](https://rapidapi.com/weatherapi/api/weatherapi-com/)                       |  
| Chainlit              | Frontend framework for user interaction.                                                                 | [Chainlit](https://docs.chainlit.io/get-started/overview)                               |  
| Python                | Backend logic for integrating OpenAI GPT and WeatherAPI.                                                 | [Python](https://www.python.org/)                                                      |  

---

## **How to Run the Chatbot**  

### **Prerequisites**  
1. **Python 3.9 or later**  
2. API Keys:  
   - **OpenAI API Key:** [Get your API key here](https://platform.openai.com/signup/).  
   - **RapidAPI Key:** [Sign up for WeatherAPI here](https://rapidapi.com/weatherapi/api/weatherapi-com/).  

### **Steps to Run**  

1. **Clone the Repository:**  
   ```bash  
   git clone https://github.com/monikagiemela/weather_chatbot.git 
   cd weather-chatbot  
   ```  

2. **Install Dependencies:**  
   Install all required libraries using the `requirements.txt` file:  
   ```bash  
   pip install -r requirements.txt  
   ```  

3. **Set Up Environment Variables:**  
   Create a `.env` file in the root directory and add your API keys:  
   ```env  
   OPENAI_API_KEY=your_openai_api_key  
   RAPID_API_KEY=your_rapidapi_key  
   ```  

4. **Run the Application:**  
   Execute the main script to start the chatbot:  
   ```bash  
  chainlit run -w run.py  
   ```  

5. **Interact with the Chatbot:**  
   Use the **Chainlit interface** to interact with the chatbot. Example queries include:  
   - "What's the weather in Paris?"  
   - "Will it rain tomorrow in London?"  
   - "How windy is it today in New York?"  

---

## **Project Structure**  
```plaintext  
├── run.py                 # Main script to run the chatbot  
├── requirements.txt       # List of dependencies for the project  
├── .env                   # File to store API keys  
├── README.md              # Documentation file  
└── app/                   # Core application logic and utilities  
    ├── __init__.py        # Initialization file for the app package  
    ├── llm.py             # Handles interactions with the OpenAI model (GPT-4o-mini)  
    ├── sys_config.py      # Manages system configurations (e.g., environment variables)  
    ├── utils.py           # Contains helper functions for the chatbot (e.g., formatting, API calls)  


```  

---

## **Future Improvements**  
- **Multi-Day Forecasts:** Enable extended weather forecasts for up to a week.  
- **Multilingual Support:** Allow chatbot interactions in multiple languages.  
- **Platform Integration:** Deploy on popular messaging platforms such as Telegram, Slack, and WhatsApp.  
- **Performance Monitoring:** Implement real-time logging and analytics to optimize user experience.  

---

## **Contributing**  
Contributions are welcome! If you'd like to contribute:  
1. Fork the repository.  
2. Create a new branch for your feature or bugfix.  
3. Submit a pull request with a detailed description of your changes.  

---

## **Acknowledgments**  
Special thanks to:  
- **[OpenAI](https://openai.com):** For providing the GPT-4o-mini model.  
- **[RapidAPI](https://rapidapi.com):** For enabling live weather data retrieval via WeatherAPI.  
- **[Chainlit](https://docs.chainlit.io/):** For the user-friendly frontend framework.  

---

## **License**  
This project is licensed under the MIT License.  

---

Feel free to reach out if you have any questions or feedback about this project!  
