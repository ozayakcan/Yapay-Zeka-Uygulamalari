# -*- coding: utf-8 -*-
#pip install speechRecognition

#pip install gTTS

#pip install playsound


import speech_recognition as sr
import webbrowser as webbrowser
import datetime as datetime
import time

from gtts import gTTS
from playsound import playsound
import random
import os

r = sr.Recognizer();

def record(ask=False):
    with sr.Microphone() as source:
        if ask:
            speak(ask)
        audio = r.listen(source)
        voice = ""
        try:
            voice = r.recognize_google(audio, language="tr-TR")
        except sr.UnknownValueError:
            speak("Söylediğinizi anlayamadım.")
        except sr.RequestError:
            speak("Bir hata oluştu.")
        return voice

def dispose(voice):
    if "nasılsın" in voice:
        speak("İyiyim sen nasılsın?")
    if "havalar nasıl" in voice:
        speak("Buralar yağmurlu. Oralar nasıl?")
    if "burası da yağmurlu":
        speak("Şemsiyeni almayı unutma")
    if "görüşürüz":
        speak("Görüşürüz")
        exit()
    if 'arama yap' in voice:
        search=record("ne aramak istemiştiniz")
        url="https://google.com/search?q="+search  
        webbrowser.get().open(url)
        speak(search + " ile ilgili bulduklarım")

def speak(string):
    tts = gTTS(string, lang="tr")
    rand = random.randint(1, 10000)
    file = "auido-" + rand + ".mp3"
    tts.save(file)
    playsound(file)
    os.remove(file)

speak("Merhaba nasılsın")

time.sleep(1)

while 1:
    voice = record()
    print(voice)
    dispose(voice)
    