# importing all the libraries
from ast import Break
import subprocess
from matplotlib.pyplot import title
from more_itertools import take #This module is used for getting system subprocess details which are used in various commands i.e Shutdown, Sleep, etc. This module comes built-in with Python. 
import wolframalpha #used to compute expert-level answers using Wolfram’s algorithms, knowledgebase and AI technology
import pyttsx3 # used for the conversion of text to speech in a program
import tkinter #used for building GUI 
import json 
import random
import operator
import speech_recognition as sr
import datetime
import wikipedia # module to get information from Wikipedia or to perform a Wikipedia search
import webbrowser #To perform Web Search
import os
import winshell
import pyjokes
import feedparser
import smtplib
import ctypes
import time
import requests # used for making GET and POST requests
import shutil
from twilio.rest import Client # Twilio is used for making call and messages.
from clint.textui import progress
#from ecapture import ecapture as ec #To capture images from your Camera
from bs4 import BeautifulSoup #makes it easy to scrape information from web pages
import win32com.client as wincl
from urllib.request import urlopen
import googletrans
from googletrans import Translator
from gtts import gTTS
from translate import Translator
import os
import psutil # to check system utilities like cpu speed, batter, etc.

#Now we will set our engine to Pyttsx3 which is used for text to speech in Python 
# and sapi5 is Microsoft speech application platform interface we will be using this for text to speech function.
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hours= int(datetime.datetime.now().hour)
    if hours >=0 and hours <5:
        speak("Good Night sir!")
    elif hours >=5 and hours <12:
        speak("Good morning sir!")
    elif hours>=12 and hours<18:
        speak("Good afternoon sir!")
    else:
        speak("Good Evening sir!")
    assname=("Jarvis one point o")
    speak("I am your assistant ")
    speak(assname)

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognizing...")
        query=r.recognize_google(audio, language="en-in")
        print("user said: ",query,"\n")
    except Exception as e:
        print(e)
        print("Unable to recognize your voice")
        speak("Unable to recognize your voice")
        return "None"
    return query

def username():
    speak("Adnan is this you?")
    verify=takeCommand()
    if "no" in verify:
        # speak("What should i call you? ")
        uname="None"
        while(uname=="None"):
            speak("What should i call you? ")
            uname=takeCommand()
            if (uname=="Rahul"):
                speak("hello madarchod, tu fir aagaya")

            if uname != "None":
                speak("Welcome")
                speak(uname)
            
    else:
        speak("Welcoe")
        uname="adnan"
        speak(uname)
    columns = shutil.get_terminal_size().columns 
    print("#####################".center(columns))
    print("Welcome ".center(columns), uname.center(columns))
    print("#####################".center(columns))
    return uname

def convert(seconds):
	seconds = seconds % (24 * 3600)
	hour = seconds // 3600
	seconds %= 3600
	minutes = seconds // 60
	seconds %= 60
	return "%d:%02d:%02d" % (hour, minutes, seconds)

if __name__ == '__main__':
    clear = lambda: os.system('cls') # This Function will clean any command before execution of this python file
    wishMe()
    
    while True:
        def jarvis():
            r=sr.Recognizer()
            with sr.Microphone() as source:
                print("Listening...")
                r.pause_threshold=1
                audio=r.listen(source)
            try:
                query=r.recognize_google(audio, language="en-in")
                print("user said: ",query,"\n")
                return query
            except:
                pass
                return "None"
        
        query=jarvis().lower()
        if "jarvis" in query:
            uname=username()        
            while True:
                speak("How Can i help you?")
                query= takeCommand().lower()
                
                if "go to sleep" in query or "good night" in query or "don't listen" in query or "wait" in query:
                    speak("for how much time you want me to sleep")
                    speak(uname)
                    a=int(takeCommand())
                    time.sleep(a)

                elif 'exit' in query or 'goodbye' in query:
                    speak("Thanks for giving me your time")
                    break

                elif "open youtube" in query or "youtube" in query:
                    speak("What would you like to see?")
                    vid= takeCommand()
                    vid_url="https://www.youtube.com/results?search_query="+vid
                    webbrowser.open(vid_url)
                    time.sleep(10)

                elif "open google" in query or "google" in query:
                    speak("What would you like to search?")
                    search= takeCommand()
                    search_url="https://www.google.com/search?q="+search
                    webbrowser.open(search_url)
                    time.sleep(10)
                
                elif "open spotify" in query or "play music" in query or "play song" in query:
                    speak("What would you like to hear?")
                    song= takeCommand()
                    song_url="https://open.spotify.com/search/"+song
                    webbrowser.open(song_url)
                    time.sleep(10)
                
                elif "open whatsapp" in query or "whatsapp" in query:
                    speak("Opening whatsapp")
                    url="https://web.whatsapp.com/"
                    webbrowser.open(url)
                    
                
                elif "open erp" in query or "erp" in query:
                    speak("Opening erp")
                    url="https://erp.mitwpu.edu.in/AdminLogin.aspx"
                    webbrowser.open(url)
                    time.sleep(10)

                elif 'the time' in query:
                    time = str(datetime.datetime.now())
                    print(time)
                    hour = time[11:13]
                    min = time[14:16]
                    speak(f"The time is sir {hour} Hours and {min} Minutes")    

                elif 'how are you' in query:
                    speak("I am fine, Thank you")
                    speak("How are you?")

                elif "feel bad" in query or "disappointed" in query or "depressed" in query:
                    speak("i am sorry you are feeling that way, you could try listening music to feel better")
                
                elif "wikipedia" in query:
                    speak("What would you like to search?")
                    search=takeCommand()
                    # query = query.replace("wikipedia", "")
                    wiki=wikipedia.summary(search, sentences=3)
                    speak("According to wikipedia")
                    print(wiki)
                    speak(wiki)
                
                elif 'search' in query or 'play' in query:
                    
                    query = query.replace("search", "")
                    query = query.replace("play", "")   
                    url="https://www.google.com/search?q="+query      
                    webbrowser.open(url)
                    time.sleep(10)

                elif 'shutdown system' in query:
                        speak("Hold On a Sec ! Your system is on its way to shut down")
                        # subprocess.call('shutdown / s /f')
                        os.system("shutdown /s /t 1")
                
                elif "where is" in query:
                    query = query.replace("where is", "")
                    location = query
                    speak("User asked to Locate")
                    speak(location)
                    webbrowser.open("https://www.google.nl / maps / place/" + location + "")
                    time.sleep(10)

                elif "translator" in query or "translate" in query:
                    lang_dic=googletrans.LANGUAGES
                    keys=list(lang_dic.keys())
                    value=list(lang_dic.values())
                    speak("What you want to translate?")
                    phrase= takeCommand()
                    speak("Which language you want to translate to?")
                    lang= takeCommand().lower()
                    position=value.index(lang)
                    to_language= keys[position]
                    speak("do you want to listen or open in google?")
                    ans=takeCommand().lower()
                    if "google" in ans:
                        url="https://translate.google.co.in/?hl=en&sl=en&tl="+to_language+"&text="+phrase+"&op=translate"
                        webbrowser.open(url)
                        
                    else:
                        translator= Translator(to_lang=to_language)
                        translation = translator.translate(phrase)
                        # translator = Translator()
                        # text_to_translate = translator.translate(phrase,src="en",dest= to_lang)
                        # text = text_to_translate.text
                        speak = gTTS(text=translation, lang=to_language)
                        speak.save("text.mp3")
                        os.system("start text.mp3")
                        
                    time.sleep(10)

                elif "write a note" in query or "make a note" in query:
                    speak("Making note ...What would be the title?")
                    title=takeCommand()
                    title=title+".txt"
                    try:
                        file=open(title,'w')
                        speak("What should i write?")
                        note=takeCommand()
                        if note == "None":
                            speak("Try again...")
                            note=takeCommand()
                        time = str(datetime.datetime.now())
                        file.write(time)
                        file.write(" :- \n")
                        file.write(note)
                        speak("note created sucessfully")
                    except:
                        speak("could not create note, try again")
                
                elif "read note" in query or "show note" in query:
                    speak("Which note you want me to read?")
                    note=takeCommand()
                    note=note+".txt"
                    try:
                        file=open(note)
                        speak("The note says")
                        speak(file.read())
                        print(file.read())

                    except:
                        speak("could not find note, try again")
                
                elif "will you be my gf" in query or "will you be my bf" in query:  
                    speak("I'm not sure about, may be you should give me some time")
                
                elif "battery" in query or "battery percent" in query or "pc is charged" in query:
                    battery= psutil.sensors_battery()
                    speak(f"Your system's battery percent is {battery.percent} percent")
                    if battery.power_plugged is True:
                        speak("Your system is currently charging ")
                    else:
                        speak("you system can last for ")
                        battery_left=convert(battery.secsleft)
                        speak(f"{battery_left[0]} hours and {battery_left[2]+battery_left[3]} minutes")

                
                

                else:
                    speak("That may be beyond my capabities right now")

        else:
            continue
            
            
            
            


                





