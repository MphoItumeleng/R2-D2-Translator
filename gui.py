import tkinter as tk
from tkinter import messagebox
from morse_translator import lettersToMorseCode, morseCodeToLetters
import time
from playsound import playsound
import os

def play_morse(morse_code):
    try:
        for char in morse_code:
            if char == '.':
                playsound(os.path.join("sounds", "dot.wav"))
            elif char == '-':
                playsound(os.path.join("sounds", "dash.wav"))
            time.sleep(0.2)
    except Exception as e:
        print(f"❌ Sound Error: {e}")
        messagebox.showerror("Sound Error", f"Could not play Morse code.\n\n{e}")

def encode():
    text = input_box.get("1.0", tk.END).strip()
    if not text:
        messagebox.showwarning("Input Error", "Please enter text to encode.")
        return
    morse = lettersToMorseCode(text)
    output_box.delete("1.0", tk.END)
    output_box.insert(tk.END, morse)
    play_morse(morse.replace(' ', ''))  # Remove spaces to play smoothly

def decode():
    code = input_box.get("1.0", tk.END).strip()
    if not code:
        messagebox.showwarning("Input Error", "Please enter Morse code.")
        return
    text = morseCodeToLetters(code)
    output_box.delete("1.0", tk.END)
    output_box.insert(tk.END, text)

# GUI setup
root = tk.Tk()
root.title("🔊 R2-D2's Morse Code Translator")

tk.Label(root, text="Input:").pack()
input_box = tk.Text(root, height=5, width=50)
input_box.pack()

tk.Button(root, text="Encode to Morse", command=encode).pack(pady=5)
tk.Button(root, text="Decode to Text", command=decode).pack(pady=5)

tk.Label(root, text="Output:").pack()
output_box = tk.Text(root, height=5, width=50)
output_box.pack()

tk.Label(root, text="May the Force be with your dots and dashes.").pack(pady=10)

root.mainloop()
