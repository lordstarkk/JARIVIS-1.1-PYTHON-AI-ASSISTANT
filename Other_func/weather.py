import json
import requests
import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
rate = engine.getProperty('rate')
engine.setProperty('rate', 140)

def say(speak):
    pyttsx3.speak(speak)

def current_weather(city):
    url = f"https://api.weatherapi.com/v1/current.json?key=e845b84953e5460abe290910240506&q={city}&aqi=yes"
    r = requests.get(url)
    wdic = json.loads(r.text)
    temp = wdic["current"]["temp_c"]
    last_updt_at = wdic["current"]["last_updated"]
    country = wdic["location"]["country"]
    last_updted = wdic["current"]["last_updated"]
    condition = wdic["current"]["condition"]["text"]
    feellike = wdic["current"]["feelslike_c"]
    heatidx = wdic["current"]["heatindex_c"]

    print(f"The current temprature in {city} is {temp} degree celcius, Feels like {feellike} degree celcius")
    say(f"The current temprature in {city} is {temp} degree celcius, Feels like {feellike} degree celcius")

    say(f"Condition is{condition}")
    print(f"Condition: {condition}")

    say(f"Heat index: {heatidx}")
    print(f"Heat index: {heatidx}")

    print(f"Country: {country} ")

    say(f"Last updated at:{last_updted}")
    print(f"Last updated at: {last_updted}")
    # print("Wether by WEATHER API - STARK")

def current_temp(city):
    url = f"https://api.weatherapi.com/v1/current.json?key=e845b84953e5460abe290910240506&q={city}&aqi=yes"
    r = requests.get(url)
    wdic = json.loads(r.text)
    feellike = wdic["current"]["feelslike_c"]
    temp = wdic["current"]["temp_c"]
    print(f"The current temprature in {city} is {temp} degree celcius, Feels like {feellike} degree celcius")
    say(f"The current temprature in {city} is {temp} degree celcius, Feels like {feellike} degree celcius")