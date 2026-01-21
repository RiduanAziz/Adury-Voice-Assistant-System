# Adury-AI-Voice-Assistant

Adury is a Python-based voice assistant that interacts with users through speech recognition, executes automation tasks, and uses Generative AI to answer open-ended questions. It is designed as a modern desktop assistant inspired by Iron Man’s JARVIS — offering hands-free control, productivity, and intelligent responses.

This project uses speech recognition, text-to-speech (TTS), web automation, and LLM integration to deliver a dynamic and customizable assistant experience.

---

## 🛠 Features

### 🔹 Basic Voice Interaction
- Greets the user based on the time of day  
- Converts speech to text using Google Speech Recognition  
- Speaks responses using **pyttsx3**

### 🔹 Automation Tasks
- Announces current time  
- Performs Wikipedia searches with spoken summaries  
- Opens websites (YouTube, Google, LinkedIn, etc.)  
- Launches apps (Notepad, Calculator, CMD — optional)  
- Plays random music from a folder (optional)

### 🔹 Generative AI Integration (The “Brain”)
- Uses **OpenAI** or **Google Gemini API**  
- Answers questions, explains concepts, writes poems, and more  
- Automatically activates when the user asks non-basic questions

### 🔹 Extra Utility & Fun
- Jokes and casual small talk  
- Easy to extend with your own custom commands

---

## 💻 Requirements

- Python **3.11+**
- Working microphone  
- API key for OpenAI (or Gemini) — optional but recommended  

---

## 🚀 How to Run Adury

1. **Create a virtual environment:**
   ```bash
   conda create -n adury python=3.11 -y
   ```

2. **Activate the environment:**
   ```bash
   conda activate adury
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Place API Key**
   ```bash
   GEMINI_API_KEY = "Your API Key Here"
   ```

5. **Run the assistant:**
   ```bash
   python adury.py
   ```

6. **For exe file conversion:**
   ```bash
   pip install pyinstaller
   ```

   ```bash
   pyinstaller --onefile adury.py
   ```

---

## 📁 Project Structure

```
Adury-Voice-Assistant-System/
│
├── logs/
│   └── application.log
├── music/
│   └── music.mp3
├── .gitignore
├── adury.ipynb
├── adury.py
├── LICENSE
├── requirements.txt
└── README.md
```

Optional folders you may add later:

```
music/        # For music playback
modules/      # For separating commands into files
data/         # For logs or saved info
```

---

## 👨‍💻 Author

**Riduan Aziz**  
Inspired by Tony Stark’s JARVIS — built for learning, automation, and AI experimentation.

---

## 📜 License

This project is open-source and free for educational and personal use.

```
    ___      _                     
   /   \__ _| |_ _   _ _ __ _   _  
  / /\ / _` | __| | | | '__| | | | 
 / /_// (_| | |_| |_| | |  | |_| | 
/___,' \__,_|\__|\__,_|_|   \__, | 
                            |___/  
      A d u r y   A I   V o i c e   A s s i s t a n t

```