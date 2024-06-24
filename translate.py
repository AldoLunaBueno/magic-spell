from googletrans import Translator

dest_lang = "es"
text = "Asta, this is what you've always done. You have a way of making the impossible possible.\nBut do not have any magic! How could we get at grimoire and that sword? What kind of freak-up nature are I now?!"

def translate_text(text, dest_lang="es"):
    translator = Translator(service_urls=['translate.google.com'])
    result = translator.translate(text, dest=dest_lang)
    return result.text

translated_text = translate_text(text, dest_lang)
print(translated_text)