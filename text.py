from googletrans import Translator

def translate_to_many_languages(text_to_translate, dest_languages):
    translator = Translator()
    translations = {}
    for lang_code, lang_name in dest_languages.items():
        translated_text = translator.translate(text_to_translate, src="en", dest=lang_code)
        translations[lang_name] = translated_text.text
    return translations

text_to_translate = input("Enter text to translate: ")


destination_languages = {
    "hi": "Hindi",
    "es": "Spanish",
    "fr": "French",
    "de": "German",
    "zh-CN": "Chinese (Simplified)",
    "te": "Telugu",
    "ta": "Tamil"
}

translations = translate_to_many_languages(text_to_translate, destination_languages)


for lang_name, translation in translations.items():
    print(f"{lang_name}: {translation}")
