from morse_translator import lettersToMorseCode, morseCodeToLetters

def main():
    print("🚀 R2-D2’s Morse Code Translator")
    mode = input("Type 'encode' to convert text to Morse, or 'decode' to convert Morse to text: ").lower()

    if mode == 'encode':
        text = input("Enter text: ")
        print("Morse Code:", lettersToMorseCode(text))
    elif mode == 'decode':
        code = input("Enter Morse code (use '/' for space between words): ")
        print("Decoded Text:", morseCodeToLetters(code))
    else:
        print("Invalid option. Please choose 'encode' or 'decode'.")

if __name__ == "__main__":
    main()
