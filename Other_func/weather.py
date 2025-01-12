# Import necessary libraries
import json
import requests
import pyttsx3
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get the API key from environment variables (to avoid hardcoding in the code)
api_key = os.getenv("WEATHER_API_KEY")

# Initialize the text-to-speech engine
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)  # Set the voice
rate = engine.getProperty("rate")
engine.setProperty("rate", 180)  # Set the speaking rate


# Function to speak the input text
def say(speak):
    pyttsx3.speak(speak)


# Function to get the current weather of a given city
def current_weather(city):
    """
    Function to fetch and display the current weather of a given city using the WeatherAPI.
    """
    url = f"https://api.weatherapi.com/v1/current.json?key=e845b84953e5460abe290910240506&q={city}&aqi=yes"  # Use the API key from the .env file
    r = requests.get(url)
    wdic = json.loads(r.text)
    print(wdic)

    # Extract relevant weather information from the response
    temp = wdic["current"]["temp_c"]
    last_updt_at = wdic["current"]["last_updated"]
    country = wdic["location"]["country"]
    last_updted = wdic["current"]["last_updated"]
    condition = wdic["current"]["condition"]["text"]
    feellike = wdic["current"]["condition"]["feelslike_c"]
    heatidx = wdic["current"]["condition"]["heatindex_c"]

    # Print and speak the weather information
    print(
        f"The current temperature in {city} is {temp} degree Celsius, Feels like {feellike} degree Celsius"
    )
    say(
        f"The current temperature in {city} is {temp} degree Celsius, Feels like {feellike} degree Celsius"
    )

    say(f"Condition is {condition}")
    print(f"Condition: {condition}")

    say(f"Heat index: {heatidx}")
    print(f"Heat index: {heatidx}")

    print(f"Country: {country} ")

    say(f"Last updated at: {last_updted}")
    print(f"Last updated at: {last_updted}")


# Function to get the current temperature of a given city
def current_temp(city):
    """
    Function to fetch and display the current temperature of a given city.
    """
    url = f"https://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=yes"  # Use the API key from the .env file
    r = requests.get(url)
    wdic = json.loads(r.text)
    print(wdic)

    # Extract relevant weather information from the response
    feellike = wdic["current"]["feelslike_c"]
    temp = wdic["current"]["temp_c"]

    # Print and speak the current temperature and feels-like temperature
    print(
        f"The current temperature in {city} is {temp} degree Celsius, Feels like {feellike} degree Celsius"
    )
    say(
        f"The current temperature in {city} is {temp} degree Celsius, Feels like {feellike} degree Celsius"
    )


current_weather("muzaffarnagar")
current_temp("muzaffarnagar")
