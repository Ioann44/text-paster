import time
import pyautogui


def simulate_typing(text):
    for char in text:
        pyautogui.write(char)


TEXT = """Text to paste"""

if __name__ == "__main__":
    time.sleep(5)
    simulate_typing(TEXT)
