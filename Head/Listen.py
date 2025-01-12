import speech_recognition as sr

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        try:
            audio = r.listen(source, timeout=3, phrase_time_limit=5)
        except sr.exceptions.WaitTimeoutError:
            print("Listening timed out, trying again.")
            return ""  # Return empty string to retry the command
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') 
        print(f"Stark: {query}\n")  
    except Exception as e:
        print("Say that again please...")  
        print("")
        return ""  # Return empty string if recognition fails
    return query
