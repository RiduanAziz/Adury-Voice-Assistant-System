# Adury-AI-Voice-Assistant

Adury is a Python-based AI voice assistant that interacts with users through speech recognition, executes automation tasks, and uses Generative AI to answer open-ended questions.
It now supports hardware control, enabling real-world automation such as lights, fans, and appliances via Arduino.

Inspired by Iron Man’s JARVIS, Adury delivers hands-free control, desktop productivity, and physical device automation in one unified system.

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

### 🔹 Hardware Automation (Smart Home)
- Control real devices using voice commands
- Communication via Serial (USB) between Python and Arduino
- Supports:
  - Bedroom Light
  - Table Lamp
  - Fan
  - TV / Appliance relay
- Expandable to more devices

Example voice commands:
- “Turn on bedroom light”
- “Switch off the fan”
- “Turn everything off”

---

## 🧠 System Architecture

```mathematica
         User Voice
            ↓
         Speech Recognition (Python)
            ↓
         Command Parser
            ↓
 ┌───────────────┬─────────────────┐
 │ Desktop Tasks │ Generative AI   │
 │ (Apps, Web)   │ (Gemini/OpenAI) │
 └───────────────┴─────────────────┘
            ↓
   Serial Communication
            ↓
         Arduino
            ↓
      Relay Module
            ↓
    Real-world Devices
```

---

# 🔌 Hardware Integration – Adury AI Voice Assistant

This document describes the **hardware-enabled extension** of the Adury AI Voice Assistant, allowing real-world device control using Arduino and relay modules.

---

## 🔌 Hardware Requirements

### ✅ Required Components
- **Arduino UNO / Nano / Mega**
- **4-Channel Relay Module (Active-LOW)**
- **USB Cable** (PC ↔ Arduino)
- **AC appliances or DC loads** *(with safety precautions)*
- **Jumper wires**
- **External power supply** *(recommended for relay stability)*

### 🔧 Optional Components
- **ESP32 / ESP8266** *(Wi-Fi upgrade)*
- **Bluetooth module** *(HC-05 / HC-06)*
- **Sensors**
  - Temperature
  - Motion
  - Gas
  - Light, etc.

---

## 🔧 Arduino Firmware (Smart Home Controller)

### Key Characteristics
- Receives **single-character commands** via Serial
- Uses **active-LOW relay logic**
- **Safe initialization** (all devices OFF at startup)

### 📟 Command Mapping

| Command | Action |
|------|------|
| `1` | Bedroom Light OFF |
| `2` | Bedroom Light ON |
| `3` | Table Lamp OFF |
| `4` | Table Lamp ON |
| `5` | Fan OFF |
| `6` | Fan ON |
| `7` | TV OFF |
| `8` | TV ON |
| `9` | All Devices OFF |
| `0` | All Devices ON |

---

## 🐍 Python ↔ Arduino Communication

- Uses **pyserial**
- Sends commands based on recognized voice input

### Example Python Command
```python
arduino.write(b'2')  # Bedroom Light ON
```

Baud rate:
```python
9600
```

---

## 💻 Requirements

- Python **3.11+**
- Working microphone  
- API key for OpenAI (or Gemini) — optional but recommended
- Arduino IDE
- USB serial drivers (CH340 if needed)

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
5. **Upload Arduino Code**
- Open Arduino IDE
- Upload Smart Home Controller sketch
- Note the COM port

6. **Run the assistant:**
   ```bash
   python adury.py
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
├── adury.ino
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

## 🔒 Safety Notice

### ⚠ Warning:
When working with AC appliances, always:
- Use relay modules with opto-isolation
- Keep low-voltage and high-voltage lines separate
- Disconnect power while wiring
- Do not exceed relay ratings

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
