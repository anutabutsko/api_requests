from datetime import datetime

import requests

USER_KEY = '2e7a860cf0ea27a3e0f6b47c4aa17204'


# get http link
def http_address(location: str):
    return f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={USER_KEY}"


def get_city_weather(location: str):
    address = http_address(location=location)

    response_data = requests.get(address).json()

    # check for invalid city name
    if response_data['cod'] == '404':
        print(f"Invalid city: {location}.\n"
              f"Please provide a valid city name.")
    else:
        main_data = response_data['main']
        api_temp = ((main_data['temp']) - 273.15)
        weather_description = response_data['weather'][0]['description']
        humidity = main_data['humidity']
        wind_speed = response_data['wind']['speed']
        date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

        print("------------------------------------------------------")
        print(f"Weather Stats for - {location.upper()} || {date_time}")
        print("------------------------------------------------------")

        print(f"Current Temperature is:         {api_temp:.2f} Degree Celsius")
        print(f"Current Weather Description:    {weather_description.title()}")
        print(f"Current Humidity:               {humidity} %")
        print(f"Current Wind Speed:             {wind_speed} kmph")


get_city_weather(input("Enter the city name: "))
