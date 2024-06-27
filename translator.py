from deep_translator import GoogleTranslator
from typing import List

def translate(text_lines: List[str], dest_lang="es") -> List[str]:
    translated_text_lines = []
    max_chars_per_batch = 5000
    batch_chars = 0
    batch_lines = []

    for index, line in enumerate(text_lines):
        line = line.strip() + "\n"
    
        if batch_chars + len(line) < max_chars_per_batch:

            batch_lines.append(line)
            batch_chars += len(line)   
            if index < len(text_lines) -1: # is last line?
                continue
        
        translated_batch_lines = __translate_batch__(batch_lines, dest_lang)

        batch_lines.clear()
        batch_lines = [line]
        batch_chars = len(line)      
                               
        translated_text_lines.extend(translated_batch_lines)

    return translated_text_lines

def __translate_batch__(batch_lines: List[str], dest_lang: str):
    batch_text = "".join(batch_lines)
        # NotValidLength error
    translated_batch_lines = (GoogleTranslator(source='auto', target=dest_lang)
                                .translate(batch_text)
                                .split("\n"))
                            
    return translated_batch_lines

# This would be useful for unit testing:
# lines = []
# with open("en_complete_text.txt", mode="r", encoding="utf-8") as f:
#     lines = f.readlines()

# with open("en.txt", mode="w", encoding="utf-8") as f:
#     f.writelines([line.strip()+"\n" for line in lines])

# with open("es.txt", mode="w", encoding="utf-8") as f:
#     trans_lines = translate(lines)
#     f.writelines([line+"\n" for line in trans_lines])
