# weather_api/weather_service.py

import requests
import os

API_KEY = os.getenv('OPENWEATHER_API_KEY')  # Make sure your API key is stored as an environment variable
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def fetch_weather_data(city):
    """Fetch weather data for a specific city."""
    params = {
        'q': city,
        'appid': API_KEY
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching data for {city}: {response.status_code}")
        return None
