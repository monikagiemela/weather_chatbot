import re
import os
from datetime import datetime

import requests
import dateparser

def determine_days_from_today(user_message):
    """
    Determines the number of days from today based on the user's input message.

    Parameters:
        user_message (str): A string containing the user's query related to the day 
                            (e.g., "What is the weather tomorrow?", "Forecast for next week").
    
    Returns:
        int: The number of days from today that corresponds to the specified time in the user message.
             - Returns 0 for "today" or "current" weather queries.
             - Returns 1 for "tomorrow" queries.
             - Returns the number of days if the query contains a phrase like "in X days".
             - Returns 7 for "next week" queries.
             - If a specific date is mentioned (e.g., "October 30" or "December 1, 2023"), calculates 
               and returns the days difference from today to that date.
             - Defaults to 0 if no specific day or date is identified in the user message.
    
    Notes:
        - Uses natural language processing via `dateparser` to interpret specific dates.
        - Assumes future dates if a specific date is parsed.
    """

    user_message = user_message.lower()
    today = datetime.now()

    if "tomorrow" in user_message:
        return 1
    elif "today" in user_message or "current" in user_message:
        return 0
    
    # "In X days" pattern
    in_days_match = re.search(r"in (\d+) days", user_message.lower())
    if in_days_match:
        return int(in_days_match.group(1))
    
    # "Next week"
    if "next week" in user_message.lower():
        return 7
    
    # Parse specific date if provided (e.g., "October 30" or "December 1, 2023")
    specific_date = dateparser.parse(user_message, settings={'PREFER_DATES_FROM': 'future'})
    if specific_date:
        days_difference = (specific_date - today).days
        if days_difference >= 0:
            return days_difference
    
    # Default to current weather if no clear forecast period is found
    return 0

def handle_weather_query(user_message, location):
    """
    Processes a user's message to determine the number of forecast days and fetches weather data for the specified location.

    Parameters:
    user_message (str): The user's input message, used to determine how many days of forecast are requested.
    location (str): The location (city, region, or coordinates) for which the weather data is being requested.

    Returns:
    dict: A JSON response from the WeatherAPI containing weather data, which includes current conditions and forecast based on the number of days determined from the message.

    Notes:
    - The function uses `determine_days_from_today` to extract the forecast duration from the user's message.
    - It then calls `get_weather` with the determined number of forecast days and the specified location.
    """
    days = determine_days_from_today(user_message)  # Get days from message
    return get_weather(location, days)

def get_weather(location, days=0):
    """
    Fetches weather data for a specified location using the WeatherAPI.

    Parameters:
    location (str): The location (city, region, or coordinates) for which the weather is being requested.
    days (int, optional): The number of days for the weather forecast. Default is 0, which returns current weather data.

    Returns:
    dict: A JSON response from the WeatherAPI containing weather data, which includes current conditions and forecast (if `days` > 0).
    
    Raises:
    Exception: If the request to the WeatherAPI fails or encounters an error, the exception is raised.
    
    Notes:
    - The function uses an API key stored in the environment variable `RAPID_API_KEY`.
    - The function supports both current weather queries (default) and forecast queries (if `days` > 0).
    - The API request has a timeout set to 10 seconds for response.
    """

    RAPID_API_KEY = os.getenv("RAPID_API_KEY")
    if days:
        querystring = {"q": location, "days": days}
    else:
        querystring = {"q": location}

    print(f"\n>>>> got the querystring as: {querystring}")
    headers = {
        "X-RapidAPI-Key": RAPID_API_KEY,
        "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
    }

    try:
        url = "https://weatherapi-com.p.rapidapi.com/forecast.json"

        response = requests.get(url, headers=headers, params=querystring, timeout=10)
        response_json = response.json()
        print(f"\n>>>> got the RAPID API response as: \n{response_json}")
        return response_json
    except Exception as e:
        raise e