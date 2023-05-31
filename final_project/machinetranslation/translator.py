"""
Translator Module

Este módulo contiene funciones para traducir texto de inglés a francés y de francés a inglés utilizando el servicio
de IBM Watson Language Translator.
"""

from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

# Autenticación
authenticator = IAMAuthenticator('e_RsjLG7lBI_6S_NDCZGdB9_HSZoAkVPKJlTlNNY3KEO')
language_translator = LanguageTranslatorV3(version='2018-05-01', authenticator=authenticator)
language_translator.set_service_url('https://api.au-syd.language-translator.watson.cloud.ibm.com/instances/5845cb2a-0c88-4786-bbf5-dcb6c1912c28')


def english_to_french(english_text):
    """
    Translates English text to French.
    """
    translation = language_translator.translate(text=english_text, model_id='en-fr').get_result()
    translated_text = translation['translations'][0]['translation']
    print(f"Translated text: {translated_text}")
    return translated_text


ENGLISH_TEXT = "Hello, how are you today?"
translated_text_1 = english_to_french(ENGLISH_TEXT)


def french_to_english(french_text):
    """
    Translates French text to English.
    """
    translation = language_translator.translate(text=french_text, model_id='fr-en').get_result()
    translated_text = translation['translations'][0]['translation']
    print(f"Translated text: {translated_text}")
    return translated_text


FRENCH_TEXT = "Bonjour comment vas tu aujourd'hui?"
translated_text_2 = french_to_english(FRENCH_TEXT)
