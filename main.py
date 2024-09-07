import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
import pygame
import os
from gtts import gTTS
recognizer=sr.Recognizer()
engine=pyttsx3.init()
newsapi="78dbab0737f8468bbfb3a41b9784bc24"
def speak_old(text):
    engine.say(text)
    engine.runAndWait()
def speak(text):
      tts=gTTS(text)
      tts.save('temp.mp3')
      # Initialize pygame mixer
      pygame.mixer.init()

# Load the MP3 file
      pygame.mixer.music.load('temp.mp3')  # Replace 'your_file.mp3' with the path to your MP3 file

# Play the MP3 file
      pygame.mixer.music.play()

# Keep the program running while the music is playing
      while pygame.mixer.music.get_busy():  # Check if the music is still playing
       pygame.time.Clock().tick(10)
       
def processCommand(c):
      if "open google" in c.lower():
            webbrowser.open("https://google.com")
      elif "open facebook" in c.lower():
            webbrowser.open("https://facebook.com")
      elif "open youtube" in c.lower():
            webbrowser.open("https://youtube.com")
      elif "open linkedin" in c.lower():
            webbrowser.open("https://linkedin.com")
      elif "open instagram" in c.lower():
            webbrowser.open("https://instagram.com")
      elif c.lower().startswith("play"):
            song=c.lower().split(" ")[1]
            link=musicLibrary.music[song]
            webbrowser.open(link)
      elif "hello" in c.lower():
            r=requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
            if r.status_code==200:
                  data=r.json()
                  aritcles=data.get('articles',[])
                  for article in aritcles:
                        speak(article['title'])
            else:
            #Let openai handle the request
                pass

if __name__=="__main__":
    speak("Initializing Jarvis....")
    #listen for the wake word "Jarvis"
    while True:
        r=sr.Recognizer()
        
        print("recognizing....")
        try:
            with sr.Microphone() as source:
                    print("Listening.....")
                    audio=r.listen(source,timeout=2)
            word=r.recognize_google(audio)
            if(word.lower()=="jarvis"):
                  speak("Ya")
                  #Listen for command
                  with sr.Microphone() as source:
                        print("Jarvis Active.....")
                        audio=r.listen(source)
                        command=r.recognize_google(audio)
                        processCommand(command)
             
        except Exception as e:
                    print("Error; {0}".format(e))