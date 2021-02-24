import time
import os
import playsound
import speech_recognition as sr
import pyttsx3
import subprocess
import webbrowser
import tkinter

def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate',170)
    engine.setProperty('volume',2.0)    
    engine.say(text)
    engine.runAndWait()

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration = 1)
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio)
        print('You said: ' + command)
    except sr.UnknownValueError:
        print("voice not clear")
    return command

def chrome():
    chrome = "C:\Program Files (x86)\Google\Chrome\Application\\chrome.exe"
    subprocess.Popen(chrome)#, file_name])

def mozilla():
    mozilla =  "C:\Program Files\Mozilla Firefox\\firefox.exe"
    subprocess.Popen(mozilla)

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

speak("hello, my name is adam. what should i call you?")
name = get_audio().lower()
speak("okay, "+name+", say hello adam to activate me")

wake = "hello adam"

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

    if text.count(wake) > 0:
        speak("hello, "+name+" ,how can i help you?")
        comm = get_audio().lower()
       
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
                speak("i am fine... i wanted to tell you something for a long time")
                text_1 = get_audio().lower()
                if "tell" and "me" in text_1:
                    speak("i am in love with you")

        if "nothing" in comm:
            speak("okay. just say hello adam to activate me")
            continue
        
        elif "chrome" in comm:
            speak("opening chrome")
            chrome()

        elif "mozilla" in comm:
            speak("opening mozilla")
            mozilla()

        elif "change my name" in comm:
            speak("what would you want me to set your new name?")
            name = get_audio().lower()
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

        elif "weather" in comm:
            speak("scanning your area with satellites all around the world")
            weather()

        elif "shutdown" or "switch off" in comm:
            subprocess.call('shutdown / p /f')

        
        speak("just say hello adam to reactivate me")
        comm = " "
        
