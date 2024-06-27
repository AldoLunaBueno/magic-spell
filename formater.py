from typing import Tuple, List
import splitter
from faster_whisper.transcribe import Word
from copy import deepcopy
Lines = Tuple[List[float], List[float], List[str], List[List[Word]]]

def format(en_lines: Lines, translated: List[str], line_limit: int) -> Tuple[List[float], List[float], List[str]]:
    copy_start_lines = en_lines[0][:]
    copy_end_lines = en_lines[1][:]
    copy_text_lines = en_lines[2][:]
    copy_translated = translated[:]

    _, _, text_list, words_list = en_lines
    index = 0
    for text, words, trans_text in zip(text_list, words_list, translated):
        if len(text) <= line_limit:
            index += 1
            continue
        s_list, e_list, t_list = splitter.smart_split(text, words, line_limit)
        copy_start_lines[index:index+1] = s_list
        copy_end_lines[index:index+1] = e_list
        copy_text_lines[index:index+1] = t_list
        
        copy_translated[index:index+1] = splitter.split_by_length(trans_text, [len(t) for t in t_list])


        index += len(s_list)
    return copy_start_lines, copy_end_lines, copy_text_lines, copy_translated
