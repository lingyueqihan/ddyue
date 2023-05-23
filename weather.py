import requests
from datetime import datetime

# Set your OpenWeatherMap API key and city ID
api_key = "YOUR_API_KEY"
city_id = "CITY_ID"

# API URL
url = f"http://api.openweathermap.org/data/2.5/weather?id={city_id}&appid={api_key}&units=metric"

while True:
    try:
        # Get current weather data from OpenWeatherMap API
        response = requests.get(url)
        data = response.json()

        # Extract temperature and weather description
        temp = data["main"]["temp"]
        desc = data["weather"][0]["description"]

        # Convert timestamp to datetime object and format the time string
        dt = datetime.fromtimestamp(data["dt"])
        time_str = dt.strftime("%Y-%m-%d %H:%M:%S")

        # Display the current time and weather information
        print(f"{time_str} \nTemperature: {temp}°C\nDescription: {desc}\n")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
    
    # Refresh every 30 minutes
    time.sleep(1800)
