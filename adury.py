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
import sys
import google.generativeai as genai
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume


LOG_DIR = "logs"
LOG_FILE = "application.log"
os.makedirs(LOG_DIR, exist_ok=True)

logging.basicConfig(
    filename=os.path.join(LOG_DIR, LOG_FILE),
    format="[ %(asctime)s ] %(levelname)s - %(message)s",
    level=logging.INFO,
)

LINKEDIN_URL = "https://www.linkedin.com/in/riduan-aziz"
MUSIC_FOLDER = os.path.expanduser("C:\\Users\\USER\\Downloads\\Adury-Voice-Assistant-System\\Music")

engine = pyttsx3.init("sapi5") if sys.platform.startswith("win") else pyttsx3.init()
engine.setProperty("rate", 170)
voices = engine.getProperty("voices")
if voices:
    engine.setProperty("voice", voices[0].id)

def speak(text):
    if not text:
        return
    print("Adury:", text)
    engine.say(text)
    engine.runAndWait()
    logging.info(f"Speak: {text}")

def takecommand():
    """This function takes command & recognize"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}\n")
        return query.lower()

    except Exception as e:
        logging.info(e)
        print("Say that again please!")
        return None

def greeting():
    hour = datetime.datetime.now().hour
    if hour < 12:
        speak("Good Morning, Sir.")
    elif hour < 18:
        speak("Good Afternoon, Sir.")
    else:
        speak("Good Evening, Sir.")
    speak("I am Adury. How can I help you?")

def tell_time():
    t = datetime.datetime.now().strftime("%I:%M %p")
    speak(f"The time is {t}.")

def open_site(name):
    if name == "google":
        speak("Opening Google.")
        webbrowser.open("https://www.google.com")
    elif name == "youtube":
        speak("Opening YouTube.")
        webbrowser.open("https://www.youtube.com")
    elif name == "linkedin":
        speak("Opening LinkedIn.")
        webbrowser.open(LINKEDIN_URL)

def wiki_search(topic):
    try:
        speak(f"Searching Wikipedia for {topic}")
        result = wikipedia.summary(topic, sentences=2)
        speak(result)
    except:
        speak("I couldn't find anything on Wikipedia for that.")

def gemini_model_response(query):
    try:
        GEMINI_API_KEY = "Your API Key Here"
        genai.configure(api_key=GEMINI_API_KEY)
        model = genai.GenerativeModel("gemini-2.5-flash")
        prompt = f"Answer the provided question in short, Question: {query}"
        response = model.generate_content(query)
        return response.text if response else "I couldn't generate a response."

    except Exception as e:
        logging.error(f"Gemini Error: {e}")
        return "Sorry, I couldn't get a response from the AI model."

def take_note(text):
    folder = "notes"
    os.makedirs(folder, exist_ok=True)
    ts = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = os.path.join(folder, f"note_{ts}.txt")
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)
    speak("Note saved.")

def play_music():
    if not os.path.isdir(MUSIC_FOLDER):
        speak("Music folder not found.")
        return
    files = [f for f in os.listdir(MUSIC_FOLDER) if f.lower().endswith((".mp3", ".wav", ".m4a"))]
    if not files:
        speak("No music found in the music folder.")
        return
    song = random.choice(files)
    path = os.path.join(MUSIC_FOLDER, song)
    speak(f"Playing {song}")
    try:
        if sys.platform.startswith("win"):
            os.startfile(path)
        else:
            subprocess.call(["xdg-open", path])
    except:
        speak("I couldn't play the music.")


def set_volume(percent):
    try:
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))

        percent = max(0, min(100, percent))  # clamp
        volume_level = percent / 100
        volume.SetMasterVolumeLevelScalar(volume_level, None)
        speak(f"Volume set to {percent} percent.")
    except:
        speak("I couldn't adjust the volume.")

def volume_up():
    try:
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))
        current = volume.GetMasterVolumeLevelScalar()
        new = min(1.0, current + 0.10)
        volume.SetMasterVolumeLevelScalar(new, None)
        speak("Volume increased.")
    except:
        speak("Failed to increase volume.")

def volume_down():
    try:
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))
        current = volume.GetMasterVolumeLevelScalar()
        new = max(0.0, current - 0.10)
        volume.SetMasterVolumeLevelScalar(new, None)
        speak("Volume decreased.")
    except:
        speak("Failed to decrease volume.")

def gemini_model_response(query):
    try:
        GEMINI_API_KEY = "Your API Key Here"
        genai.configure(api_key=GEMINI_API_KEY)
        model = genai.GenerativeModel("gemini-2.5-flash")
        prompt = f"Answer the provided question in short, Question: {query}"
        response = model.generate_content(prompt)
        return response.text if response else "I couldn't generate a response."

    except Exception as e:
        logging.error(f"Gemini Error: {e}")
        return "Sorry, I couldn't get a response from the AI model."

def main():
    greeting()
    time.sleep(1)

    while True:
        query = takecommand()

        if query is None:
            continue

        logging.info("Command: " + query)

        if "your name" in query:
            speak("My name is Adury.")
        elif "time" in query:
            tell_time()
        elif query.startswith("wikipedia"):
            topic = query.replace("wikipedia", "").strip()
            if topic:
                wiki_search(topic)
            else:
                speak("Please tell me what to search.")
        elif "open google" in query:
            open_site("google")
        elif "open youtube" in query:
            open_site("youtube")
        elif "open linkedin" in query:
            open_site("linkedin")
        elif "play music" in query or "play song" in query:
            play_music()
        elif "take note" in query or "note" in query:
            text = query.replace("take note", "").replace("note", "").strip()
            if not text:
                speak("What should I note?")
                text = takecommand()
            if text:
                take_note(text)
        elif "thank you" in query:
            speak("You're welcome, Sir.")
        elif query in ("exit", "quit", "stop", "bye"):
            speak("Goodbye Sir. Have a great day.")
            break
        elif "volume up" in query or "increase volume" in query:
            volume_up()

        elif "volume down" in query or "decrease volume" in query:
            volume_down()

        elif "mute" in query:
            set_volume(0)

        elif "unmute" in query:
            set_volume(50)  

        elif "set volume to" in query:
            try:
                num = int(query.replace("set volume to", "").replace("percent", "").strip())
                set_volume(num)
            except:
                speak("Please say a valid percentage.")

        else:
            speak("Let me think.")
            answer = gemini_model_response(query)
            speak(answer)
            logging.info("Gemini Response: " + answer)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        speak("Shutting down.")
