
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import pywhatkit
import sys
import subprocess
import time


current_time = time.localtime()
pywhatkit.sendwhatmsg("+923203533038", "hello", current_time.tm_hour, current_time.tm_min + 1)

# foe gui from index.html file 
url = 'http://127.0.0.1:5500/index.html'
webbrowser.open(url)

# for voice
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 174)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    
    speak("hello,I am jerry, How can I assist you")
    
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        
    try:
        print("Recognizing...")        
        query = r.recognize_google(audio, language='en-US')
        print(f"User said: {query}\n")
        
        
    except Exception as e:
        print("Say that again please..")
        speak("say that again please..")
        return "None"  # Returning "None" may cause infinite loop issues





if __name__=="__main__":
    # speak("hy how are you") 
    wishMe()
    while True:
        query=takeCommand().lower()
        if 'who is' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
            
        elif 'open youtube' in query:
            speak('Searching youtube')
            webbrowser.open("https://www.youtube.com")
            
        elif 'open google' in query:
            speak('Searching google')
            webbrowser.open("https://www.google.com")
        
        
            
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"time is {strTime}")
            # for 12hr (%I:%M %p)
        
        elif "date" in query:
            current_date = datetime.datetime.now().strftime("%b %d, %Y")
            speak(f"Today's date is {current_date}")
        
        
        elif 'snake game' in query:
            speak('Opening Snake Game')
            subprocess.Popen(['python', 'snake.py'])
        
        elif 'tictac game' in query:
            speak('Opening tictac Game')
            subprocess.Popen(['python', 'game.py'])  
        
            
        elif "open calculator" in query:
            webbrowser.open("https://www.google.com/search?q=Calculator")
        
        elif "play" in query:
            song = query.replace('play', "")
            speak("playing" + song)
            pywhatkit.playonyt(song)
            
        elif 'search' in query:
            # speak('What should I search')
            speak('Searching on Google')
            query = query.replace("search", "")
            webbrowser.open(f"https://www.google.com/search?q={query}")
        
        elif 'how' in query:
            # speak('What should I search')
            speak('Searching on youtube')
            query = query.replace("search", "")
            webbrowser.open(f"https://www.youtube.com/search?q={query}")
            
        elif "send message" in query:
            speak('sending message')
            current_time = time.localtime()
            pywhatkit.sendwhatmsg("+923203533038", "hello", current_time.tm_hour, current_time.tm_min + 1)


        
        elif "no" in query:
            speak("thank you for useing me,have a nice day")    
            sys.exit()
            
        
        
        speak('Do you have any other Question')
        
    
  
        
