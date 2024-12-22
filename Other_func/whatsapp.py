#importing requireds modules
import pywhatkit
import datetime
from Head.Listen import *
from Head.speak import *

#defining hour and minutes
minu = datetime.datetime.now().minute
hour = datetime.datetime.now().hour

contacts = {
    "contact name" : "contact nunber"
    #Add more here
}


#function to send whatsapp message (make sure you are login on whatsapp web)
def SendWhatsMsg():
    print("Whom do you want to send message")
    say("Whom do you want to send message?")
    name = takeCommand().lower()
    number = contacts.get(name)
    if name in contacts:
        try:
            print("What is the message you want to send?")
            say("What is the message you want to send?")
            msg = takeCommand().lower()
            msg = msg.capitalize()
            msg = pywhatkit.sendwhatmsg(number, msg, hour,minu)
        except:
            print("Error")
            say("Sorry sir an error has occurred, i couldn't send this message")
    else:
        print(f"{number}not found in database")
        say(f"Sorry sir i couldn't found {number} in my data")