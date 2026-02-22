import pyautogui
import time
import pyperclip
from google import genai


client = genai.Client(api_key="")


pyautogui.click(1208, 1054)
time.sleep(1)

run_count = 0
chat_context = []

while True:
    run_count += 1
    print(f"\n--- Scan {run_count} started ---")

    
    pyautogui.moveTo(538, 144)
    pyautogui.mouseDown(button='left')
    pyautogui.dragTo(1831, 932, duration=2.0, button='left')
    pyautogui.mouseUp(button='left')

    pyautogui.hotkey('ctrl', 'c')
    pyautogui.click()
    time.sleep(1)

    chat_history = pyperclip.paste().strip()
    print("WhatsApp Text:\n", chat_history)

   
    if not chat_history:
        print("No new message detected.")
        time.sleep(2)
        continue

    chat_context.append({"author": "user", "content": chat_history})

    
    system_prompt = (
        "You are Harry, a coder from India who speaks Hindi and Bengali. "
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


   
    chat_context.append({"author": "assistant", "content": assistant_reply})

    
    pyperclip.copy(assistant_reply)
    pyautogui.click(829, 950)  # WhatsApp input box
    time.sleep(0.5)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(0.5)
    pyautogui.press('enter')

    print("\nAI Response Sent:\n", assistant_reply)

   
    if run_count >= 1:
        print("Automation complete — exiting program.")
        break

    time.sleep(2)
