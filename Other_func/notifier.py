from notifypy import Notify
import schedule
import time
import datetime

icon_path = "add notification icon path here"
def Notification():
    notification = Notify()
    notification.title = "Jarvis AI"
    notification.message = "JARVIS is activated and ready to help you and assist you."
    notification.application_name = "J.A.R.V.I.S"
    notification.icon = icon_path
    # notification.audio = 
    notification.send()

def no_internetNotfication():
    notification = Notify()
    notification.title = "No internet"
    notification.message = "Your internet is Gone"
    notification.application_name = "J.A.R.V.I.S"
    notification.icon = icon_path
    # notification.audio = 
    notification.send()

def Internet_back_notification():
    notification = Notify()
    notification.title = "Internet Back"
    notification.message = "Internet is back! You g=can now give me commands"
    notification.application_name = "J.A.R.V.I.S"
    notification.icon = icon_path
    # notification.audio = 
    notification.send()

schedule.every().run