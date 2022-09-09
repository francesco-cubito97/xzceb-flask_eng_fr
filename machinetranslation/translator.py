"""
This is the module that implements the translation functions from english to french
and viceversa
"""

import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ["apikey"]
url = os.environ["url"]

authenticator = IAMAuthenticator(f"{apikey}")
language_translator = LanguageTranslatorV3(
    version="1.0",
    authenticator=authenticator
)

language_translator.set_service_url(f"{url}")

def english_to_french(englishText):
    """
    Translate english text to french text
    """
    frenchText = language_translator.translate(englishText, "en-fr").get_result()
    
    return json.dumps(frenchText)["translations"][0]["translation"]

def french_to_english(frenchText):
    """
    Translate french text to english text
    """
    englishText = language_translator.translate(englishText, "fr-en").get_result()
    
    return json.dumps(englishText)["translations"][0]["translation"]

print(english_to_french("Hello to everyone"))