"""
Jarvis - Clean Voice Assistant
Author: You :)
Features:
- Wake word "Jarvis"
- Time, Wikipedia, Jokes, System control
- Offline speech recognition with Vosk
- Text-to-speech replies
"""

import os
import datetime
import webbrowser
import pyttsx3
import wikipedia
import pyjokes
import pyautogui
import psutil

# Speech recognition
from vosk import Model, KaldiRecognizer
import pyaudio
import json

# ================= SETTINGS =================
WAKE_WORD = "jarvis"
VOSK_MODEL_PATH = "vosk-model-small-en-us-0.15"   # folder where you unzipped vosk model
SAMPLE_RATE = 16000
CHUNK = 4000
# ============================================

# Init TTS
engine = pyttsx3.init()
engine.setProperty("rate", 170)
voices = engine.getProperty("voices")
if voices:
    engine.setProperty("voice", voices[0].id)

def speak(text):
    print("Jarvis:", text)
    engine.say(text)
    engine.runAndWait()

def handle_command(cmd):
    """Handle recognized commands"""
    cmd = cmd.lower()

    if "time" in cmd:
        speak(f"The time is {datetime.datetime.now().strftime('%I:%M %p')}")
    elif "open youtube" in cmd or "youtube" in cmd:
        webbrowser.open("https://youtube.com")
        speak("Opening YouTube")
    elif "joke" in cmd:
        speak(pyjokes.get_joke())
    elif "screenshot" in cmd:
        filename = f"screenshot_{datetime.datetime.now().strftime('%H%M%S')}.png"
        pyautogui.screenshot(filename)
        speak("Screenshot taken.")
    elif "battery" in cmd:
        battery = psutil.sensors_battery()
        if battery:
            speak(f"Battery at {battery.percent} percent.")
        else:
            speak("I cannot read the battery status.")
    elif "who is" in cmd or "what is" in cmd:
        topic = cmd.replace("who is", "").replace("what is", "").strip()
        try:
            summary = wikipedia.summary(topic, sentences=2)
            speak(summary)
        except:
            speak("Sorry, I couldn't find that on Wikipedia.")
    elif "shutdown" in cmd:
        speak("Shutting down system.")
        os.system("shutdown /s /t 5")
    else:
        speak("Sorry, I didn't understand.")

def listen_loop():
    """Main loop: listen for wake word then commands"""
    if not os.path.exists(VOSK_MODEL_PATH):
        print(f"❌ Vosk model not found! Please unzip into: {VOSK_MODEL_PATH}")
        return

    model = Model(VOSK_MODEL_PATH)
    recognizer = KaldiRecognizer(model, SAMPLE_RATE)

    mic = pyaudio.PyAudio()
    stream = mic.open(format=pyaudio.paInt16, channels=1,
                      rate=SAMPLE_RATE, input=True,
                      frames_per_buffer=CHUNK)
    stream.start_stream()

    print(f"🎤 Listening for wake word: {WAKE_WORD}")

    listening = False

    while True:
        data = stream.read(CHUNK, exception_on_overflow=False)
        if recognizer.AcceptWaveform(data):
            result = recognizer.Result()
            text = json.loads(result).get("text", "").lower()

            # Debug: show everything heard
            if text.strip():
                print(f"📝 Heard: {text}")

            if not listening:
                if WAKE_WORD in text:
                    speak("Yes?")
                    listening = True
            else:
                if text.strip():
                    handle_command(text)
                listening = False

if __name__ == "__main__":
    print("🚀 Jarvis starting...")
    listen_loop()