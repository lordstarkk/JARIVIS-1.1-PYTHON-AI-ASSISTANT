import smtplib
import speech_recognition as sr
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os
from Head.speak import *
from Head.Listen import *

# Load environment variables from .env file
load_dotenv()

# Get sensitive data from the .env file
SENDER_EMAIL = os.getenv("SENDER_EMAIL")
SENDER_PASSWORD = os.getenv("SENDER_PASSWORD")

# Predefined list of recipients and their corresponding emails
mails = {
    "name": "recipient_email@example.com",
    # Add more entries as needed
}

def SendMails():
    # Ask the user for the recipient name
    say("Whom should I send the mail?")
    print("Tell me the name of the receiver")
    
    # Take command from the user to get the recipient name
    recipient = takeCommand().lower()

    # Get the email address for the recipient
    recipientMail = mails.get(recipient)
    
    if recipientMail:
        # Initialize the SMTP server
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()

        # Login to the sender's email account
        s.login(SENDER_EMAIL, SENDER_PASSWORD)
        
        # Ask for the subject of the email
        print("What's the subject?")
        say("What is the subject of this mail?")
        subject = takeCommand()

        # Ask for the message content
        print("What is the message?")
        say("What is the message?")
        msg = f"{takeCommand()}\n\nThis message is sent by Stark's virtual assistant JARVIS."

        # Send the email
        s.sendmail(SENDER_EMAIL, recipientMail, f'Subject: {subject}\n\n{msg}')
        
        try:
            # Notify the user about the mail being sent
            print("Sending mail...")
            say("Sending mail, sir.")
        except Exception as e:
            print("Could not send the email.")
            say("Sorry, sir, I could not send this mail.")
        
        # Close the SMTP session
        s.quit()
        
        # Confirm that the email was successfully sent
        print("Mail was sent successfully.")
        say("Mail was sent successfully, Sir. What else can I do for you?")
    
    else:
        # If the recipient is not found, notify the user
        print(f"{recipient} not found.")
        say(f"Sorry, sir, I could not find {recipient} in my memory.")
