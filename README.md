

---

# 🧠 Jarvis AI Voice Assistant

## 📖 Story

This project began with the simple idea of **making my own Jarvis-like voice assistant** at age 13. At first, I tried using large AI models like GPT, but installing them caused issues with **Torch, Transformers, and dependencies**. Since I wanted something simple, fast, and that works **offline**, we rebuilt Jarvis step by step.

The final product is a **clean, lightweight Python assistant** that:

* Uses **Vosk** (offline speech recognition) so it doesn’t need the internet to listen.
* Speaks back using **pyttsx3**.
* Listens only when I call it by name (**wake word: "Jarvis"**).
* Can answer basic questions with **Wikipedia** and **jokes**.
* Can **open YouTube, tell the time, take screenshots, check battery, and even shutdown the system**.
* Works like a personal desktop assistant, running in the background and responding to commands.

---

## ⚡ Features

* 🎤 **Wake Word Detection** – Only responds when you say *“Jarvis”*.
* 🗣️ **Text-to-Speech** – Replies in a natural voice using `pyttsx3`.
* 🔎 **Wikipedia Search** – Get quick 2-sentence summaries.
* 😂 **Jokes** – Lighten the mood with random jokes.
* ⏰ **Time Announcements** – Ask for the current time.
* 🖼️ **Screenshots** – Instantly take and save screenshots.
* 🔋 **Battery Status** – Check laptop/PC battery levels.
* ▶️ **Open YouTube** – Opens YouTube in browser.
* 💻 **System Control** – Shutdown command supported.

---

## 🛠️ Installation

1. **Clone or download the project folder**.

2. Install dependencies:

   ```bash
   pip install vosk pyaudio pyttsx3 wikipedia pyjokes pyautogui psutil
   ```

3. Download the **Vosk English Model**:
   👉 [vosk-model-small-en-us-0.15.zip](https://alphacephei.com/vosk/models)

4. Unzip it into your project folder:

   ```
   project/
     jarvis.py
     vosk-model-small-en-us-0.15/
   ```

5. Run the assistant:

   ```bash
   python jarvis.py
   ```

---

## 🚀 Usage

* Run the program → You’ll see:

  ```
  🚀 Jarvis starting...
  🎤 Listening for wake word: jarvis
  ```

* Say: **“Jarvis”** → Jarvis replies *“Yes?”*.

* Give a command:

  * “What is Shahrukh Khan?”
  * “Tell me a joke”
  * “Open YouTube”
  * “Take screenshot”
  * “What’s the time”
  * “What’s the battery”
  * “Shutdown”

---

## 🔮 Future Enhancements

* Add **system volume & brightness controls**.
* Add **Spotify / Music playback**.
* Integrate **smart home controls**.
* Add **chat-based AI (like GPT)** when internet is available.

---

## 🎯 Final Product

You now have a **personal Jarvis** that:

* Runs offline.
* Listens for your call.
* Speaks and executes commands.
* Can be expanded as your coding skills grow.

This project is not just code — it’s proof that with patience, debugging, and curiosity, anyone (even at 13!) can **build their own AI assistant**. 🚀

---

👉 Do you want me to also make this README into a **PDF file** so you can show it as your project report at school?
