from deep_translator import GoogleTranslator
from typing import List, Tuple
def translate(text_lines: List[float], dest_lang="es") -> List[str]:
    text = "\n".join(text_lines)
    translated_text_lines = (GoogleTranslator(source='auto', target='es')
                             .translate(text)
                             .split("\n"))
    return translated_text_lines