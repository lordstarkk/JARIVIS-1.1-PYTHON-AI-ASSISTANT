from notifypy import Notify
import schedule
import time
import datetime

def Notification():
    notification = Notify()
    notification.title = "Jarvis AI"
    notification.message = "JARVIS is activated and ready to help you and assist you."
    notification.application_name = "J.A.R.V.I.S"
    notification.icon = "C:\\Users\\Admin\\Downloads\\jarvisp.jpeg"
    # notification.audio = 
    notification.send()

schedule.every().run