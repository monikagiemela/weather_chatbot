import re
import os
from datetime import datetime

import requests
import dateparser

def determine_days_from_today(user_message):
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
    days = determine_days_from_today(user_message)  # Get days from message
    return get_weather(location, days)

def get_weather(location, days=0):
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