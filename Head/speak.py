# Import necessary libraries
import os
import pyttsx3
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize pyttsx3 engine
engine = pyttsx3.init()

# Retrieve voice settings from environment variables
voice_id = int(os.getenv("VOICE_ID", 0))  # Default to voice[0] if not set
voice_rate = int(os.getenv("VOICE_RATE", 180))  # Default rate 180 if not set

# Set voice properties
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[voice_id].id)
engine.setProperty('rate', voice_rate)

def say(speak):
    """
    Function to speak the given text.
    """
    pyttsx3.speak(speak)
