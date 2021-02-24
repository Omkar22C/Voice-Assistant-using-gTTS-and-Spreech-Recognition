import time
import os
import playsound
import speech_recognition as sr
import pyttsx3
import subprocess

def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
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

wake = "hello john"
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

    if num == 0:
        speak("hello i am john. what should i call you")
        name = get_audio().lower()
        num = 1

    elif num == 1:
        if text.count(wake) > 0:
            speak("hello, ",name,", how can i help you?")
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
                    speak("i am fine... i wanted to tell you something for a long time")
                    text_1 = get_audio().lower()
                    if "tell" and "me" in text_1:
                        speak("i am in love with you")

            
            '''            

            if "chrome" in text:
                speak("opening chrome")
                chrome()

            if "mozilla" in text:
                speak("opening mozilla")
                mozilla()

            '''
            
