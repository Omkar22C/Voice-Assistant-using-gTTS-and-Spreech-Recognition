import time
import os
import playsound
import speech_recognition as sr
#import pyttsx3
import subprocess
import webbrowser
import tkinter
import requests
import datetime
import wolframalpha
from gtts import gTTS

'''
def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate',170)
    engine.setProperty('volume',2.0)    
    engine.say(text)
    engine.runAndWait()
'''

def speak(text):
    tts = gTTS(text = text, lang = 'en-us')
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)


def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration = 1)
        audio = r.listen(source)
    #try:
    command = r.recognize_google(audio)
    print('You said: ' + command)
    #except sr.UnknownValueError:
    #print("voice not clear")
        
        
    return command


def chrome():
    chrome = "C:\Program Files (x86)\Google\Chrome\Application\\chrome.exe"
    subprocess.Popen(chrome)#, file_name])

def mozilla():
    mozilla =  "C:\Program Files\Mozilla Firefox\\firefox.exe"
    subprocess.Popen(mozilla)

def pdf():
    pdf = "C:\Program Files (x86)\Adobe\Acrobat Reader DC\Reader\\AcroRd32.exe"
    subprocess.Popen(pdf)
    

def weather():
    api_key = "Api key" 
    base_url = "http://api.openweathermap.org / data / 2.5 / weather?"
    speak("tell the City name ")  
    city_name = get_audio().lower() 
    complete_url = base_url + "appid =" + api_key + "&q =" + city_name 
    response = requests.get(complete_url)  
    x = response.json()  
      
    if x["cod"] != "404":  
        y = x["main"]  
        current_temperature = y["temp"]  
        current_pressure = y["pressure"]  
        current_humidiy = y["humidity"]  
        z = x["weather"]  
        weather_description = z[0]["description"]  
        speak("here are the weather details")
        print(" Temperature (in kelvin unit) = " +str(current_temperature)+"\n atmospheric pressure (in hPa unit) ="+str(current_pressure) +"\n humidity (in percentage) = " +str(current_humidiy) +"\n description = " +str(weather_description))  
      
    else:  
        speak(" City Not Found ") 

speak("hello, my name is amanda. what should i call you?")
name = "rijul"

speak("okay, "+name+" , say hello amanda to activate me")

wake = "hello amanda"
num = 0

'''
service = authent_google()
text = get_audio()
get_events(get_date(text),service)
print(get_date(text))
'''

while True:
    text=get_audio().lower()

    HOW_STRS = ["open"]
    NOTE_STRS = ["how are you"]
    THINGS_STR = ["what things can you do"]

    if text.count(wake) > 0:
        speak("hello, "+name+" ,how can i help you?")
        try:
            comm = get_audio().lower()
        except :
            speak("sorry i didn't hear you")
            continue

        
       
        '''
        for phrase in NOTE_STRS:
            if phrase in text:
                speak("what would you want me to say?")
                note_text = get_audio().lower()
                #note(note_text)
                speak(note_text + " rijul")
        '''
        for shabd in NOTE_STRS:
            if shabd in comm:
                speak("i am fine. thanks for asking. how are you?")

                try:
                    text_1 = get_audio().lower()
                except :
                    speak("sorry i didn't hear you")
                    continue

                if "i" and "am" in text_1:
                    if "good" or "fine" in text:
                        speak("great!")

                    else:
                        speak("may i ask the reason for your upsetness?")
                        try:
                            feel = get_audio().lower()

                        except :
                            speak("sorry i didn't hear you")
                            continue

                        speak("don't worry, you will be fine")

        for words in THINGS_STR:
            if words in comm:
                speak("i can open softwares, browse famous sites, surf the web and switch off your laptop")
                continue

        if "nothing" in comm:
            speak("okay. just say hello amanda to activate me")
            continue
            
        elif "chrome" in comm:
            speak("opening chrome")
            chrome()

        elif "mozilla" in comm:
            speak("opening mozilla")
            mozilla()

        elif "change my name" in comm:
            speak("what would you want me to set your new name?")

            try:
                name = get_audio().lower()
            except :
                speak("sorry i didn't hear you")
                continue

            speak("okay, "+name+" ,i have changed your name in my database")

        elif "youtube" in comm:
            speak("opening youtube")
            webbrowser.open("youtube.com")

        elif "google" in comm:
            speak("opening google")
            webbrowser.open("google.com")

        elif "wikipedia" in comm:
            speak("opening wikipedia")
            webbrowser.open("wikipedia.com")

        elif "facebook" in comm:
            speak("opening facebook")
            webbrowser.open("facebook.com")

        elif "weather" in comm:
            speak("scanning your area with satellites all around the world")
            weather()

        elif "time" and "now" in comm:
            abhi = datetime.datetime.now()
            print(abhi)
            speak("the time has been displayed on the screen!")
            
        elif "shutdown" or "switch off" in comm:          
            option = get_audio().lower()
            subprocess.call('shutdown / p /f')

        elif "pdf" and "reader" in comm:
            speak("opening p,d,f reader")
            pdf()

        elif "what is" in query or "who is" in query: 
            client = wolframalpha.Client("API_ID") 
            res = client.query(query) 
              
            try: 
                print (next(res.results).text) 
                speak (next(res.results).text) 
            except StopIteration: 
                print ("No results")
        
        speak("just say hello amanda to reactivate me")

        

        
