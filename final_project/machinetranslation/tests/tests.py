import unittest
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

class TranslationTest(unittest.TestCase):
    def setUp(self):
        api_key = '7-YtKCIk4IQCg2HqMlLS82N_xEfXH729xos4nm-QFBix'
        service_url = 'https://api.jp-tok.language-translator.watson.cloud.ibm.com/instances/9b72f585-6a7f-4c47-afe0-439daf19f6af'
        authenticator = IAMAuthenticator(api_key)
        self.language_translator = LanguageTranslatorV3(
            version='2018-05-01',
            authenticator=authenticator
        )
        self.language_translator.set_service_url(service_url)

    def test_english_to_french_translation(self):
        text_to_translate = 'Hello'
        expected_translation = 'Bonjour'
        
        model_id = 'en-fr'
        translation = self.language_translator.translate(
            text=text_to_translate,
            model_id=model_id
        ).get_result()
        
        translated_text = translation['translations'][0]['translation']
        self.assertEqual(translated_text, expected_translation)
    
    def test_null_english_input_translation(self):
        text_to_translate = None
        
        model_id = 'en-fr'
        translation = self.language_translator.translate(
            text=text_to_translate,
            model_id=model_id
        ).get_result()
        
        translated_text = translation['translations'][0]['translation']
        self.assertIsNone(translated_text)

    def test_french_to_english_translation(self):
        text_to_translate = 'Bonjour'
        expected_translation = 'Hello'
        
        model_id = 'fr-en'
        translation = self.language_translator.translate(
            text=text_to_translate,
            model_id=model_id
        ).get_result()
        
        translated_text = translation['translations'][0]['translation']
        self.assertEqual(translated_text, expected_translation)
    
    def test_null_french_input_translation(self):
        text_to_translate = None
        
        model_id = 'fr-en'
        translation = self.language_translator.translate(
            text=text_to_translate,
            model_id=model_id
        ).get_result()
        
        translated_text = translation['translations'][0]['translation']
        self.assertIsNone(translated_text)

if __name__ == '__main__':
    unittest.main()