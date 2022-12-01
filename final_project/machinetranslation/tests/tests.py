import unittest
from ibm_cloud_sdk_core import ApiException
from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase):
    def testEqual(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        self.assertEqual(english_to_french('Yes'), 'Oui')

    def testNull(self):
        try:
            english_to_french('')
        except ApiException as e:
            self.assertEqual(e.code, 400)
            self.assertEqual(e.message, 'Unable to validate payload size, the \'text\' is empty.')

class TestFrenchToEnglish(unittest.TestCase):
    def testEqual(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        self.assertEqual(french_to_english('Merci'), 'Thank you')

    def testNull(self):
        try:
            french_to_english('')
        except ApiException as e:
            self.assertEqual(e.code, 400)
            self.assertEqual(e.message, 'Unable to validate payload size, the \'text\' is empty.')

unittest.main()