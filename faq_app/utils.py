from googletrans import Translator, LANGUAGES
import logging

logger = logging.getLogger(__name__)

def translate_text(text, target_lang):
    translator = Translator()
    try:
        translation = translator.translate(text, dest=target_lang)
        return translation.text if translation else text
    except Exception as e:
        logger.error(f"Translation error: {e}")
        return text  # Return original text if translation fails

def get_supported_languages():
    return list(LANGUAGES.keys())

