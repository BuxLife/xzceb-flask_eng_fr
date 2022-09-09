"""
Translation tests for translator.py
"""
import unittest

from machinetranslation import translator
from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase):
    """
    Test translation from english to french
    """
    def test_english_to_french(self):
        """
        Test null assertion
        Test string assertion
        """
        self.assertNotEqual(translator.english_to_french("Hello"), None)
        self.assertEqual(translator.english_to_french("Hello"), "Bonjour")
        print("Test 1 assertions complete (assertNotEqual, assertEqual)")

class TestFrenchToEnglish(unittest.TestCase):
    """
    Test translation from french to english
    """
    def test_french_to_english(self):
        """
        Test null assertion
        Test string assertion
        """
        self.assertNotEqual(translator.french_to_english("Bonjour"), None)
        self.assertEqual(translator.french_to_english("Bonjour"), "Hello")
        print("Test 2 assertions complete (assertNotEqual, assertEqual)")

if __name__=='__main__':
    unittest.main()
