🤖 WhatsApp Auto Reply AI Chatbot (Gemini Powered)

This project is a Python-based automation bot that reads WhatsApp chat messages, sends them to Google Gemini AI, generates a smart reply, and automatically pastes the response back into WhatsApp chat—just like a real conversational assistant.

It uses:

🖱️ PyAutoGUI → to control mouse & keyboard

📋 Pyperclip → to handle clipboard

⏳ Time → for delays

🤖 Google Gemini (genai) → to generate intelligent replies

✨ Features

✔️ Automatically scans WhatsApp screen chat
✔️ Copies conversation text
✔️ Sends text to Gemini AI
✔️ Generates contextual reply
✔️ Pastes reply into WhatsApp input box
✔️ Sends message automatically
✔️ Works in Real-Time

🛠️ Requirements
🔹 Software Needed

Windows PC

WhatsApp Desktop

Python 3.9+

📦 Install Dependencies

Run:

pip install pyautogui
pip install pyperclip
pip install google-genai

🔑 Add Gemini API Key

Replace:

client = genai.Client(api_key="YOUR_API_KEY")


with your actual key from:
https://aistudio.google.com/apikey

▶️ How It Works

1️⃣ Bot clicks WhatsApp window to focus
2️⃣ Selects chat area by dragging the mouse
3️⃣ Copies chat text
4️⃣ Sends text to Gemini AI with persona prompt
5️⃣ Gets AI reply
6️⃣ Copies reply to clipboard
7️⃣ Pastes reply into WhatsApp chat box
8️⃣ Presses Enter to send message

All automatically 🎯
