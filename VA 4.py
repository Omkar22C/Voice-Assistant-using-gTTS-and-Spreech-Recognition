import time
import os
import playsound
import speech_recognition as sr
import pyttsx3
from gtts import gTTS
import subprocess

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
    subprocess.Popen(chrome)

def mozilla():
    mozilla =  "C:\Program Files\Mozilla Firefox\\firefox.exe"
    subprocess.Popen(mozilla)

wake = "hello john"
num = 0


while True:
    text=get_audio().lower()
    
    HOW_STRS = ["open"]
    NOTE_STRS = ["how are you", "how was your day","how is life"]
    
    if text.count(wake) > 0:
        
        if num == 0:
            speak("by what name should i call you?")
            name = get_audio().lower()
            speak("okay, "+name+(".  say hello john to activate me"))
            num+= 1
        
        elif num == 1:
            speak("hello.  "+name+".  how can i help you")
            text = get_audio().lower()
            
            '''
            for phrase in NOTE_STRS:
                if phrase in text:
                    speak("what would you want me to say?")
                    note_text = get_audio().lower()
                    #note(note_text)
                    speak(note_text + " rijul")
            '''
            for shabd in NOTE_STRS:
                if shabd in text:
                    speak("i am fine. how can i be a help for you")
                    text_1 = get_audio().lower()
            
            if "what things" or "what all" in text:
                speak("i can do the following things")
                speak("i can open an app")
                speak("i can switch off your laptop")

            elif "nothing" in text:
                continue
            
            elif "chrome" in text:
                speak("opening chrome")
                chrome()

            elif "mozilla" in text:
                speak("opening mozilla")
                mozilla()

            elif "change my name" in text:
                speak("what would you want me to set your new name?")
                name = get_audio().lower()
                speak("okay, "+name+" ,i have changed your name in my database")
                
            speak("if you want me to do something else, just say hello john")

