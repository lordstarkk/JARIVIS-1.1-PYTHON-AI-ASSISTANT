# Import necessary libraries
import pywhatkit
import datetime
from dotenv import load_dotenv
import os

# Import functions for listening and speaking
from Head.Listen import *
from Head.speak import *

# Load environment variables from .env file
load_dotenv()

# Get contact numbers from environment variables (stored securely in .env)
contacts = {"name": os.getenv("CONTACT_NAME")}  # Add more in .env as needed

# Get current time for scheduling messages
minu = datetime.datetime.now().minute
hour = datetime.datetime.now().hour


def SendWhatsMsg():
    """
    Function to send a WhatsApp message using pywhatkit.
    """
    print("Whom do you want to send message?")
    say("Whom do you want to send message?")

    # Listen for the recipient's name
    name = takeCommand().lower()
    number = contacts.get(name)

    if name in contacts:
        try:
            print("What is the message you want to send?")
            say("What is the message you want to send?")

            # Listen for the message to send
            msg = takeCommand().lower()
            msg = msg.capitalize()

            # Schedule and send the message
            pywhatkit.sendwhatmsg(number, msg, hour, minu)
        except:
            # Handle any errors in sending the message
            print("Error")
            say("Sorry sir, an error has occurred, I couldn't send this message")
    else:
        # Handle cases where the contact is not found
        print(f"{name} not found in database")
        say(f"Sorry sir, I couldn't find {name} in my data")
