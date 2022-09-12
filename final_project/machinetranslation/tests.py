import unittest
from translator import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):
    def test_e2f(self):
        self.assertNotEqual(english_to_french("Hello").lower(), " ".lower())
        self.assertEqual(english_to_french("Hello").lower(), "Bonjour".lower())

    def test_f2e(self):
        self.assertNotEqual(french_to_english("Bonjour").lower(), " ".lower())
        self.assertEqual(french_to_english("Bonjour").lower(), "Hello".lower())

if __name__ == '__main__':
    unittest.main()