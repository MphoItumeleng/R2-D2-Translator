import unittest
from morse_translator import lettersToMorseCode, morseCodeToLetters

class TestMorseCodeTranslator(unittest.TestCase):
    def test_encode(self):
        self.assertEqual(
            lettersToMorseCode("Help me Obi-Wan!"),
            ".... . .-.. .--. / -- . / --- -... .. -....- .-- .- -. -.-.--"
        )

    def test_decode(self):
        self.assertEqual(
            morseCodeToLetters(".... .- ...- . / -.-- --- ..- / ... . . -. / .-. --- -... --- -.. ..-.-"),
            "HAVE YOU SEEN ROBODU?"
        )

if __name__ == '__main__':
    unittest.main()
