from Other_func.weather import *
from Head.Listen import *
from Head.speak import *
import wikipedia
from Other_func.mailsender import *
import datetime
import webbrowser
import smtplib
from requests import get
import pywhatkit as kit
import pyautogui as pgui
from Other_func.whatsapp import *
from Other_func.notifier import *
from Other_func.calculator import *
import psutil 

battery = psutil.sensors_battery()
time = datetime.datetime.now().strftime("%H:%M:%S") 
hour_min = datetime.datetime.now().strftime("%H:%M")

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=6 and hour<12:
        say("Good Morning Sir!")

    elif hour>=12 and hour<18:
        say("Good Afternoon Sir!")
       
    elif hour>= 0 and hour<5:
        say("Sir you aren't slept? how man i help you")

    else:
        say("Good Evening Sir!") 

def convertTime(seconds): 
    minutes, seconds = divmod(seconds, 60) 
    hours, minutes = divmod(minutes, 60) 
    return "%d:%02d:%02d" % (hours, minutes, seconds) 

def batteryRemaining():
    battery = psutil.sensors_battery() 
    batteryRemaining = convertTime(battery.secsleft)

    RemainingTime = f"{batteryRemaining} is left"
    print(RemainingTime)


def battery_percent():
    battery = psutil.sensors_battery()
    btry_percent = (f"Battery percentage: {battery.percent}%")
    print(btry_percent)
    say(f"Currently Battery is {battery.percent}%")

def batteryPlugged():

    plugged =  battery.power_plugged
    if plugged == True:
        print("Status: Charging")
        say("Status: Charging")
        return True
    else:
        print("Status: Not charging") 
        say("battery is not charging") 
        return False


def restart():
   os.system("shutdown /r /t 0")

def shutdown():
    os.system("shutdown /s /t 0") 

def logout():
   os.system("shutdown /l")

def news():
    n_url =  "https://newsapi.org/v2/top-headlines?country=in&category=science&sortby=popularity&apiKey=Enter your api key here"
    nr = requests.get(n_url).json()
    articles = nr["articles"]
    head = []
    day = ["First", "Second", "Third", "Forth", "Fifth"]
    for ar in articles:
        head.append(ar["title"])
    say("Here are top 5 news of today")
    for i in range (len(day)):
        print(f" {day[i]} news is {head[i]}")
        say(f"Today's {day[i]} news is {head[i]}")

def closewindow():
    pgui.hotkey('alt', 'f4')

if __name__ == '__main__':
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
    print("Program Created By STARK \nInstagram: strangexstark_")

    while True:
        query = takeCommand().lower()

        if "wikipedia" in query:
            say("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2) 
            say("According to Wikipedia")
            print(results)
            say(results)

        if "the time" in query:
            time = datetime.datetime.now().strftime("%H:%M:%S") 
            print(time)
            say(f"The time is {time}")

        if "close current window" in query:
            say("Closing current window")
            closewindow()
        
        if "quit" in query or "exit" in query:
            break

        elif "youtube" in query:
            if "open" in query:
                say("opening youtube sir")
                webbrowser.open("www.youtube.com")
            else:
                query.replace("jarvis", "")
                query.replace("about", "")
                query.replace("search on youtube", "")
                webbrowser.open(f"https://www.youtube.com/results?search_query={query}")

        elif "search about" in query:
            op = query
            opr = op.replace("search about", "")
            say(f"searching about {opr} on ")
            webbrowser.open(f"https://www.google.com/search?q={opr}")
        
        elif "search on internet" in query:
            op = query
            opr = op.replace("search on internet", "")
            say(f"searching about {opr} on browser")
            webbrowser.open(f"https://www.google.com/search?q={opr}")
            

        elif "open a website" in query or "open a site" in query:
            say("which site should i open sir?")
            site = takeCommand().lower()
            webbrowser.open(f"www.{site}.com")
            say(f"Opening {site}")  

        elif "open command prompt" in query:
            say("opening cammand prompt")
            os.startfile("C:\\Users\\Admin\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\Command Prompt.lnk")
        elif "are you there" in query:
            say("at your service sir!")

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
            else:
                pass
        elif "shutdown system" in query or "shutdown the system" in query:
            say("Shuting Down System")
            shutdown()
        elif "restart system" in query:
            say("Restarting the system")
            restart()
            
        elif "logout" in query:
            say("loging you out sir")
            logout()

        elif "news" in query:
            news()
                        
        elif "who are you" in query or "what are you" in query:
            print("I am J.A.R.V.I.S (Just a Rather Very Intelligent System), a Fictional A.I  Originally created by Tony Stark(Iron-man), And this program is created by Strange Stark ")
            say("I am JARVIS (Just a Rather Very Intelligent System), a Fictional A.I  Originally created by Tony Stark(Iron-man), And this program is created by Strange Stark")

        elif "what you can do" in query or "what can you do" in query:
            print("I can do many tasks like telling you weather, send mails, send whatsapp messages play music, open a website or software and many more")
            say("I can do many tasks like telling you weather, send mails, send whatsapp messages play music, open a website or software and many more")

        elif "ip address" in query or "whats my ip" in query:
            ip = get("https://api.ipify.org").text
            print(f"IP address: {ip}")
            say(f"your IP address is : {ip}")

        elif "play a song on youtube" in query:
            say("Which song should i play")
            print("Tell the name of song")
            song = takeCommand().lower()
            kit.playonyt(song)
            say(f"Playing {song} on youtube")
        
        elif "check weather" in query or "check temperature" in query:
            say("which city?")
            city = takeCommand()
            if "temperature" in query:
                current_temp(city)     
            else:
                current_weather(city)

        elif "send a whatsapp" in query or "send a message on whatsapp" in query:
            SendWhatsMsg()

        elif "calculate" in query:
            if "add" in query or "+" in query:
                soln = re.findall(r'\b\d+\b', query)
                try:
                    n1 = int(soln[0])
                    n2 = int(soln[1])
                    soln = add(n1,n2)
                    print(f"{n1} + {n2} is {soln}")
                    say(f"{n1} + {n2} is {soln}")
                except:
                    print("Error")
                    say("Sorry sir, an error has occurred")
            elif "multiply" in query or 'x' in query:
                soln = re.findall(r'\b\d+\b', query)
                try:
                    n1 = int(soln[0])
                    n2 = int(soln[1])
                    soln = multiply(n1,n2)
                    print(f"{n1} Multiply by {n2} is {soln}")
                    say(f"{n1} Multiply by {n2} is {soln}")
                except:
                    print("Error")
                    say("Sorry sir, an error has occurred")

            elif "subtract" in query or "-" in query:
                soln = re.findall(r'\b\d+\b', query)
                try:
                    n1 = int(soln[0])
                    n2 = int(soln[1])
                    soln = sub(n1,n2)
                    print(f"{n1} - {n2} is {soln}")
                    say(f"{n1} subtracted by {n2} is {soln}")
                except:
                    print("Error")
                    say("Sorry sir, an error has occurred")

            elif "divide" in query or "/" in query:
                soln = re.findall(r'\b\d+\b', query)
                try:
                    n1 = int(soln[0])
                    n2 = int(soln[1])
                    soln = divide(n1,n2)
                    print(f"{n1} Divided by {n2} is {soln}")
                    say(f"{n1} Divided by {n2} is {soln}")
                except:
                    print("Error")
                    say("Sorry sir, an error has occurred")
            else:
                say("Sorry sir, i couldn't understand what to calculate, could you please say that again")
        elif query == "jarvis":
            say("Yes sir, how can i help you?")
        elif "current weather" in query or "current temperature" in query:
            if "temperature" in query:
                current_temp("YourCityName")     
            else:
                current_weather("YourCityNam")
