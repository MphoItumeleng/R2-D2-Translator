# Dictionary for encoding
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..',

    '0': '-----', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.',

    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.',
    '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-',
    '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-',
    '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.',
    '$': '...-..-', '@': '.--.-.', ' ': '/'
}

# Reverse dictionary for decoding
MORSE_CODE_REVERSE = {v: k for k, v in MORSE_CODE_DICT.items()}

def lettersToMorseCode(text: str) -> str:
    """
    Converts plain text into Morse code.
    """
    return ' '.join(MORSE_CODE_DICT.get(char.upper(), '') for char in text)

def morseCodeToLetters(code: str) -> str:
    """
    Converts Morse code into plain text.
    """
    return ''.join(
        MORSE_CODE_REVERSE.get(symbol, '') if symbol != '/' else ' '
        for symbol in code.split(' ')
    )
