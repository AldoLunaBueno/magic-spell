from typing import Tuple, List
from faster_whisper.transcribe import Word

puncts = ".,;:?!"
start_words = [" a", " an", " the", " and", " with", " by", " across", " within", " toward", " thereby", " between", " above", " below", " for", " from"
               " but", " then", " since", " after", " before" " because", 
               " my", " your", " his", " its", " our", " their", 
               " what", " where", " when", " who", " how", " which", " why",
               " other", " another"
               ]

def smart_split(text: str, words_list: List[Word], line_limit: int):
    splitted_text_w_times = []
    rtext = text
    index = 0
    while len(rtext) > line_limit:
        ltext, rstart, index, rtext = __split__(rtext, words_list, index)
        splitted_text_w_times.extend([ltext, rstart])
    splitted_text_w_times.append(rtext)

    start_list = []
    end_list = []
    text_list = []

    start_list.append(words_list[0].start)
    text_list.append(splitted_text_w_times.pop(0))
    while len(splitted_text_w_times) > 0:
        time = splitted_text_w_times.pop(0)
        end_list.append(time)
        start_list.append(time)
        text_list.append(splitted_text_w_times.pop(0))
    end_list.append(words_list[-1].end)

    return start_list, end_list, text_list

def split_by_length(text: str, relative_lengths: List[int]) -> List[str]:
    total = sum(relative_lengths)
    lengths = [int(len(text)*r/total) for r in relative_lengths]
    split_points = [text.find(" ", length) for length in lengths[:-1]]
    splitted_text = [text[i:j].lstrip() for i,j in zip([0]+split_points, split_points+[None])]
    return splitted_text

def __split__(text: str, words_list: List[Word], index: int) -> Tuple[str, float, int, str]:
    pieces = []
    ltext = ""
    punct_found = False
    rstart = 0
    for idx, word in enumerate(words_list[index:], 0):        
        pieces.append(word.word)            
        if idx < 4:
            continue
        if word.word[-1] in puncts and not punct_found:
            punct_found = True
            continue
        if word.word in start_words or punct_found:
            pieces.pop()
            ltext = "".join(pieces)
            rstart = word.start
            break
    index += idx
    rtext_list = [word.word for word in words_list[index:]]
    rtext = "".join(rtext_list)
    return ltext, rstart, index, rtext.lstrip()


