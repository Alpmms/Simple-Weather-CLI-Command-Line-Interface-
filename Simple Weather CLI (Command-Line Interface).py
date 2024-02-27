#!/usr/bin/env python
# coding: utf-8

# In[5]:


import requests

API_KEY = "1648188fb91029225d234c6d2f334d8a"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"

def get_weather_data(city_name):
    complete_url = BASE_URL + "appid=" + API_KEY + "&q=" + city_name
    response = requests.get(complete_url)
    return response.json()

def process_weather_data(data):
    if "main" in data:
        if data["cod"] != "404":
            main_data = data["main"]
            temperature = main_data["temp"] - 273.15  # Convert Kelvin to Celsius
            pressure = main_data["pressure"]
            humidity = main_data["humidity"]

            weather_data = data["weather"]
            weather_description = weather_data[0]["description"]

            return {
                "temperature": temperature,
                "pressure": pressure,
                "humidity": humidity,
                "description": weather_description
            }
        else:
            return None
    else:
        print("Error: Unexpected response from API")
        return None

def display_weather(weather_data):
    if weather_data is not None:
        print(f"Temperature: {weather_data['temperature']} °C")
        print(f"Atmospheric Pressure: {weather_data['pressure']} hPa")
        print(f"Humidity: {weather_data['humidity']} %")
        print(f"Weather Description: {weather_data['description'].capitalize()}")
    else:
        print("City not found!")

if __name__ == "__main__":
    city_name = input("Enter city name: ")
    weather_data = get_weather_data(city_name)
    processed_data = process_weather_data(weather_data)
    display_weather(processed_data)


# In[ ]:





# In[ ]:




