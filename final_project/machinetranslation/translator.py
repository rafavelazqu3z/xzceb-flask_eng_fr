"""
translator.py

This script demonstrates translation using IBM Watson Language Translator.
"""

import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

api_key = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(api_key)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)
language_translator.set_disable_ssl_verification(True)

ENGLISH_TEXT = "Hello, how are you today?"

def english_to_french(english_text):
    """
    Translates English text to French using the IBM Watson Language Translator.

    Args:
        english_text (str): The text to be translated.

    Returns:
        str: The translated text in French.
    """
    translation = language_translator.translate(
        text=english_text,
        model_id='en-fr'
    ).get_result()
    french_text = translation['translations'][0]['translation']
    print(f"Translated text: {french_text}")
    return french_text

translated_text = english_to_french(ENGLISH_TEXT)

def french_to_english(french_text):
    """
    Translates French text to English using the IBM Watson Language Translator.

    Args:
        french_text (str): The text to be translated.

    Returns:
        str: The translated text in English.
    """
    translation = language_translator.translate(
        text=french_text,
        model_id='fr-en'
    ).get_result()
    english_text = translation['translations'][0]['translation']
    print(f"Translated text: {english_text}")
    return english_text

french_to_english(translated_text)
