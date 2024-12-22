import speech_recognition as sr

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source,timeout=1, phrase_time_limit=5)
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') 
        # text_area.insert(tk.END, f"You said: {command}\n")
        print(f"Stark: {query}\n")  
    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        print("")
        return "None" 
    return query