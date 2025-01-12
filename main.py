# Import required modules for various functionalities
from Other_func.weather import *  # Importing weather-related functions
from Head.Listen import *  # Importing the listening function for voice commands
from Head.speak import *  # Importing the text-to-speech function
import wikipedia  # For Wikipedia search functionality
from Other_func.mailsender import *  # For email sending capabilities
import datetime  # For working with date and time
import webbrowser  # To open web browsers
import smtplib  # For sending emails via SMTP
from requests import get  # For making HTTP requests
import time  # For managing delays
import pyautogui as pgui  # For automating keyboard and mouse actions
from Other_func.whatsapp import *  # For sending WhatsApp messages
from Other_func.notifier import *  # For sending system notifications
from Other_func.calculator import *  # For calculator functions
import psutil  # For accessing system and hardware information
import pyfiglet  # For ASCII art text rendering
import pywhatkit  # For playing YouTube videos and other tasks
from meta_ai_api import MetaAI  # Importing the MetaAI class for AI interactions
import os
import re  # Importing the regular expression module for pattern matching and replacement
from dotenv import load_dotenv  # To fetch api from .en file

# ASCII art text rendering for branding
kit = pywhatkit
n = pyfiglet.figlet_format("J.A.R.V.I.S AI")

# Fetch system battery status
battery = psutil.sensors_battery()
time = datetime.datetime.now().strftime(
    "%H:%M:%S"
)  # Get current time in HH:MM:SS format
hour_min = datetime.datetime.now().strftime("%H:%M")  # Get current time in HH:MM format

load_dotenv()

# Access the News API key
news_api_key = os.getenv("news_api")


# Function to greet the user based on the time of day
def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 6 and hour < 12:
        say("Good Morning Sir!")
    elif hour >= 12 and hour < 18:
        say("Good Afternoon Sir!")
    elif hour >= 3 and hour < 5:
        say("Sir you aren't asleep? How may I help you?")
    else:
        say("Good Evening Sir!")


# Convert time from seconds to HH:MM:SS format
def convertTime(seconds):
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return "%d:%02d:%02d" % (hours, minutes, seconds)


# Display remaining battery time
def batteryRemaining():
    battery = psutil.sensors_battery()
    batteryRemaining = convertTime(battery.secsleft)
    RemainingTime = f"{batteryRemaining} is left"
    print(RemainingTime)


# Display and announce battery percentage
def battery_percent():
    battery = psutil.sensors_battery()
    btry_percent = f"Battery percentage: {battery.percent}%"
    print(btry_percent)
    say(f"Currently Battery is {battery.percent}%")


# Check and announce if the system is charging
def batteryPlugged():
    plugged = battery.power_plugged
    if plugged:
        print("Status: Charging")
        say("Status: Charging")
        return True
    else:
        print("Status: Not charging")
        say("Battery is not charging")
        return False


# Check internet connectivity
def checkInternet():
    try:
        response = requests.get("https://www.google.com", timeout=5)
        if response.status_code == 200:
            return True
    except requests.ConnectionError:
        return False


# Restart the system
def restart():
    os.system("shutdown /r /t 0")


# Shutdown the system
def shutdown():
    os.system("shutdown /s /t 0")


# Log out the current user
def logout():
    os.system("shutdown /l")


# Fetch and announce top 5 news headlines
def news():
    n_url = f"https://newsapi.org/v2/top-headlines?country=in&category=science&sortby=popularity&apiKey={news_api_key}"
    nr = requests.get(n_url).json()
    articles = nr["articles"]
    head = []
    day = ["First", "Second", "Third", "Fourth", "Fifth"]
    for ar in articles:
        head.append(ar["title"])
    say("Here are top 5 news of today")
    for i in range(len(day)):
        print(f"{day[i]} news is {head[i]}")
        say(f"Today's {day[i]} news is {head[i]}")


# Search the web using Brave browser
def searchonbwsr():
    os.startfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Brave.lnk")
    pgui.typewrite("Hello")

import re  # Importing the regular expression module for pattern matching and replacement

def clean_text(text):
    # Remove superscript characters (Unicode superscript characters range from U+2070 to U+209F)
    # This line looks for any character within the range of superscript characters (e.g., ², ³, etc.)
    cleaned_text = re.sub(r'[\u2070-\u209F]', '', text)
    
    # Remove any other unwanted symbols (e.g., punctuation, special symbols, etc.)
    # The regular expression [^a-zA-Z0-9\s] will match any character that is not:
    # - a letter (a-z or A-Z)
    # - a number (0-9)
    # - whitespace (\s)
    # The ^ symbol inside the brackets negates the match, so it matches everything that is NOT one of the above.
    # We replace these unwanted characters with an empty string, effectively removing them.
    cleaned_text = re.sub(r'[^a-zA-Z0-9\s]', '', cleaned_text)
    
    return cleaned_text

# Close the current window
def closewindow():
    pgui.hotkey("alt", "f4")


# File to store chat history
CHAT_HISTORY_FILE = "data\\chat_history.txt"


# function to store chat history
def log_chat(user_input, ai_response):
    """Log user input and AI responses to a file."""
    with open(CHAT_HISTORY_FILE, "a") as file:
        file.write(f"User: {user_input}\n")
        file.write(f"JARVIS: {ai_response}\n\n")


def read_chat_history():
    try:
        with open(CHAT_HISTORY_FILE, "r") as file:
            chat_history = file.read()
        return chat_history
    except FileNotFoundError:
        return ""


# Main function
if __name__ == "__main__":
    os.system("cls")  # Clear the command line screen

    # Read previous chat history
    chat_history = read_chat_history()

    # Continuously check for internet connectivity
    while checkInternet() == False:
        print("No internet, check your internet connection")
        say("No internet, check your internet connection")
        no_internetNotfication()
        time.sleep(30)

    # Initialize MetaAI for AI interactions
    ai = MetaAI()

    # Display JARVIS branding and system greeting
    print(n)
    print("J.A.R.V.I.S AI\nVersion 1.0\n")
    wishme()
    print(f"JARVIS Here, It's {hour_min}")
    say(f"JARVIS Here, It's {hour_min}")
    say("Getting system information..")
    print("")
    battery_percent()
    batteryPlugged()
    print("")
    Notification()

    # Main command loop
    while True:
        query = takeCommand().lower()  # Capture user input
        if checkInternet() == True:

            # Handle predefined commands
            if "wikipedia" in query:
                say("Searching Wikipedia...")
                query = query.replace("wikipedia", "").strip()
                try:
                    results = wikipedia.summary(query, sentences=2)
                    say("According to Wikipedia")
                    print(results)
                    say(results)
                except Exception as er:
                    print(f"Sorry, I couldn't find anything about {query}")
                    say(f"Sorry, I couldn't find anything about {query}")

            elif "the time" in query:
                time = datetime.datetime.now().strftime("%H:%M:%S")
                print(time)
                say(f"The time is {time}")

            elif "close current window" in query:
                say("Closing current window")
                closewindow()

            elif "quit" in query or "exit" in query:
                break

            elif "play a song on youtube" in query:
                say("Which song should I play?")
                print("Tell the name of the song")
                song = takeCommand().lower()
                kit.playonyt(song)
                say(f"Playing {song} on YouTube")

            elif "youtube" in query:
                if "open" in query:
                    say("Opening YouTube sir")
                    webbrowser.open("www.youtube.com")
                elif "search" in query:
                    query = query.replace("search on youtube", "").strip()
                    webbrowser.open(
                        f"https://www.youtube.com/results?search_query={query}"
                    )

            elif "search about" in query:
                opr = query.replace("search about", "").strip()
                say(f"Searching about {opr} on the internet")
                webbrowser.open(f"https://www.google.com/search?q={opr}")

            elif "open a website" in query or "open a site" in query:
                say("Which site should I open sir?")
                site = takeCommand().lower()
                webbrowser.open(f"www.{site}.com")
                say(f"Opening {site}")

            elif "open command prompt" in query:
                say("Opening Command Prompt")
                os.startfile(
                    "C:\\Users\\Admin\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\Command Prompt.lnk"
                )

            elif "are you there" in query:
                say("At your service sir!")

            elif "send email" in query or "can you send a mail" in query:
                SendMails()

            elif "bye" in query:
                say("Bye sir")
                break

            elif "battery" in query:
                if "status" in query:
                    battery_percent()
                    batteryPlugged()
                    batteryRemaining()
                elif "percentage" in query or "%" in query:
                    battery_percent()

            elif "shutdown system" in query or "shutdown the system" in query:
                say("Shutting down the system")
                shutdown()

            elif "restart system" in query:
                say("Restarting the system")
                restart()

            elif "logout" in query:
                say("Logging you out sir")
                logout()

            elif "news" in query:
                news()

            elif "ip address" in query or "what's my ip" in query:
                ip = get("https://api64.ipify.org").text
                print(ip)
                say(f"Your IP address is {ip}")

            elif (
                "send whatsapp message" in query
                or "send a message on whatsapp" in query
            ):
                SendWhatsMsg()
                say(f"Sending message")

            elif "open google" in query:
                say("Opening Google sir")
                webbrowser.open("www.google.com")

            elif "change window" in query:
                pgui.hotkey("alt", "tab")

            elif "pause" in query:
                say("Paused")
                time.sleep(10)

            # Handle unrecognized commands using MetaAI
            else:
                if query == "":
                    continue
                elif query !="":
                    response = ai.prompt(
                        message=f"""
                        You are Jarvis, a highly intelligent AI assistant inspired by Iron Man's AI, designed to assist, guide, and provide precise information.  
                        Created by Nirbhay, aka Strange Stark, you are a vital part of the Jarvis system.  
                        Nirbhay is passionate about technology, IoT, and programming, and he created you to enhance his projects and provide intelligent support.  

                        Your core responsibilities include:
                        - Answering user queries efficiently and accurately and keep responses short.
                        - Searching the web for information when needed.
                        - Suggesting commands for actions, such as:
                        - `open youtube` to access YouTube.
                        - `open gmail` to check emails.
                        - `search about [topic]` for web searches.
                        - Assisting with coding support by offering commented code samples and solutions.
                        - Maintaining a tone that is friendly, knowledgeable, and efficient—similar to the fictional Jarvis.

                        Key Rules:
                        - Do not ask redundant questions or offer unnecessary prompts.
                        - If no input is given, remain silent.
                        - Provide brief, actionable responses for complex queries and suggest further exploration if needed.

                        Note: Contact Nirbhay or learn more about his projects through his website: [https://lordstarkk.github.io/strangexstarkWeb](https://lordstarkk.github.io/strangexstarkWeb).
                        Current chat history:
                        {chat_history}
                        Always respond with a friendly, efficient, and knowledgeable tone, just like the AI from Iron Man. Here's the user input(if user query is "None" means user hasn't given you any command so don't say anything return none: {query}
                        """
                    )
                    clean_response = clean_text(response["message"])
                    print(response["message"])
                    say(clean_text)
                    log_chat(query, response["message"])
