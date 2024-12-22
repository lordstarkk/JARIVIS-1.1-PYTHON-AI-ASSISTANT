import smtplib
import speech_recognition as sr
from email.mime.text import MIMEText
from Head.speak import *
from Head.Listen import *

mails = {
    "recipietent name": "recipietent mail"
    #add more here
}
def SendMails():
    say("Whom Should i send the mail")
    print("Tell me the name of reciver")
    recipient = takeCommand().lower()
    recipientMail = mails.get(recipient)
    if recipient in mails:
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login("sendermail@sender.com", "passwordHere")
        print("Whats the subject?")
        say("What is the subject of this mail")
        subject = takeCommand()
        print("What is the massage?")
        say("What is the massage?")
        msg = f"{takeCommand()}\n This Message is sent by Stark's virtual assitant JARVIS"
        s.sendmail("sendermail@sender.com", recipientMail, 'Subject: {}\n\n{}'.format(subject, msg))
        try:
            print("Sending mail..")
            say("Sending mail sir")
        except Exception as e:
            print("Could not sent")
            say("Sorry sir i could not send this mail")
        s.quit()
        print("Mail was sent Succesfully")
        say("Mail was sent Succesfully Sir. what else i can do for you")

    else:
        print(f"{recipient} not found")
        say(f"Sorry sir i could not found {recipient} in my Memory")


