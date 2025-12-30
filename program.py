import pyautogui
import time
import pyperclip
from google import genai

# --- Set your API key ---
client = genai.Client(api_key="AIzaSyA29-NhhkIy0RkFcAtHCjHUzW9cphhQXSA")

# Click WhatsApp window
pyautogui.click(1208, 1054)
time.sleep(1)

run_count = 0
chat_context = []

while True:
    run_count += 1
    print(f"\n--- Scan {run_count} started ---")

    # STEP 1: Drag to select text from WhatsApp
    pyautogui.moveTo(538, 144)
    pyautogui.mouseDown(button='left')
    pyautogui.dragTo(1831, 932, duration=2.0, button='left')
    pyautogui.mouseUp(button='left')

    # STEP 2: Copy selected text
    pyautogui.hotkey('ctrl', 'c')
    pyautogui.click()
    time.sleep(1)

    # STEP 3: Read clipboard
    chat_history = pyperclip.paste().strip()
    print("WhatsApp Text:\n", chat_history)

    # Skip if clipboard empty
    if not chat_history:
        print("No new message detected.")
        time.sleep(2)
        continue

    # STEP 4: Add user message to chat context
    chat_context.append({"author": "user", "content": chat_history})

    # STEP 5: Generate AI response
    # STEP 5: Generate AI response (safer for all SDK versions)
    system_prompt = (
        "You are Harry, a coder from India who speaks Hindi and English and Bengali. "
        "Analyze the message and respond like Harry."
    )
    contents = f"{system_prompt}\nUser message: {chat_history}"

    try:
        response = client.models.generate_content(
            model="gemini-3-flash-preview",
            contents=contents
        )
        try:
            assistant_reply = response.text.strip()
        except:
            assistant_reply = response.candidates[0].content.parts[0].text.strip()

        if not assistant_reply:
            assistant_reply = "Sorry, I couldn't generate a response."
    except Exception as e:
        print("Gemini API error:", e)
        assistant_reply = "Sorry, I couldn't generate a response."

    print("\nAI Reply Generated:\n", assistant_reply)       


    # STEP 6: Append AI response to chat context
    chat_context.append({"author": "assistant", "content": assistant_reply})

    # STEP 7: Paste AI response into WhatsApp
    pyperclip.copy(assistant_reply)
    pyautogui.click(829, 950)  # WhatsApp input box
    time.sleep(0.5)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(0.5)
    pyautogui.press('enter')

    print("\nAI Response Sent:\n", assistant_reply)

    # Stop after 1 scan (optional)
    if run_count >= 1:
        print("Automation complete — exiting program.")
        break

    time.sleep(2)
