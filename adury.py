import speech_recognition as sr
import pyttsx3
import logging
import os
import datetime
import wikipedia
import webbrowser
import random
import subprocess
import time


LOG_DIR = "logs"
LOG_FILE_NAME = "application.log"

os.makedirs(LOG_DIR, exist_ok=True)
log_path = os.path.join(LOG_DIR, LOG_FILE_NAME)

logging.basicConfig(
    filename=log_path,
    format="[ %(asctime)s ] %(levelname)s - %(message)s",
    level=logging.INFO
)


engine = pyttsx3.init("sapi5")
engine.setProperty("rate", 170)
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)


def speak(text):
    engine.say(text)
    engine.runAndWait()


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("🔍 Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}")
        return query.lower()

    except Exception as e:
        logging.error(f"Recognition Error: {str(e)}")
        print("Say that again please...")
        return "none"


def greeting():
    hour = datetime.datetime.now().hour

    if hour < 12:
        speak("Good Morning!")
    elif hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("I am Adury. How can I help you today?")


greeting()

# FIX: give a small delay so microphone doesn’t start instantly
time.sleep(1.2)

while True:
    query = takeCommand()

    if query == "none":
        continue

    print(f"Command received: {query}")

    if "your name" in query:
        print("My name is Adury.")
        speak("My name is Adury.")
        logging.info("User asked for assistant's name.")

    elif "time" in query:
        strTime = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"Sir, the time is {strTime}")
        logging.info("User asked for current time.")

    elif "how are you" in query:
        speak("I am functioning at full capacity, sir!")
        logging.info("User inquired about assistant's well-being.")

    elif "who made you" in query:
        speak("I was created by Riduan sir, a brilliant mind!")
        logging.info("User asked about assistant's creator.")

    elif "thank you" in query:
        speak("It is my pleasure sir.")
        logging.info("User expressed gratitude.")

    elif "open google" in query:
        speak("Opening Google.")
        webbrowser.open("https://www.google.com")
        logging.info("User requested to open Google.")

    elif "open youtube" in query:
        speak("Opening YouTube.")
        webbrowser.open("https://www.youtube.com")
        logging.info("User requested to open YouTube.")

    elif "open facebook" in query:
        speak("Opening Facebook.")
        webbrowser.open("https://www.facebook.com")
        logging.info("User requested to open Facebook.")

    elif "exit" in query or "quit" in query or "stop" in query:
        speak("Goodbye sir! Have a wonderful day.")
        exit()

    else:
        speak("I'm sorry, I didn't understand that. Could you repeat?")
