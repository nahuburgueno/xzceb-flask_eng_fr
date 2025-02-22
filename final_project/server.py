from machinetranslation import translator
from flask import Flask, render_template, request
from machinetranslation.translator import language_translator

import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def english_to_french(english_text):
    """
    Translates English text to French.
    """
    english_text = request.args.get('text')
    translation = language_translator.translate(text=english_text, model_id='en-fr').get_result()
    translated_text = translation['translations'][0]['translation']
    print(f"Translated text: {translated_text}")
    return translated_text


ENGLISH_TEXT = "Hello, how are you today?"
translated_text_1 = english_to_french(ENGLISH_TEXT)


@app.route("/frenchToEnglish")
def french_to_english(french_text):
    """
    Translates French text to English.
    """
    french_text = request.args.get('text')
    translation = language_translator.translate(text=french_text, model_id='fr-en').get_result()
    translated_text = translation['translations'][0]['translation']
    print(f"Translated text: {translated_text}")
    return translated_text


FRENCH_TEXT = "Bonjour comment vas tu aujourd'hui?"
translated_text_2 = french_to_english(FRENCH_TEXT)


@app.route("/")
def renderIndexPage():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
