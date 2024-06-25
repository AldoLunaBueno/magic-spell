from typing import Tuple
puncts = ".,;:?!"
start_words = ["a", "the", "and", "but", "then", "since", "after", "before" "because", "my", "your", "his", "its", "our", "their", "what", "where", "when", "who", "how"]

def smart_split(text: str, segment_words, index: int) -> Tuple[str, float, int, str]:
    pieces = []
    punct_found = False
    rstart = 0
    for idx, (start, _, word) in enumerate(segment_words[index:], 0):        
        pieces.append(word)            
        if idx < 4:
            continue
        if word[-1] in puncts and not punct_found:
            punct_found = True
            continue
        if word in start_words or punct_found:
            pieces.pop()
            ltext = " ".join(pieces)
            rtext = text.removeprefix(ltext)
            rstart = start
            break
    index += idx
    return ltext, rstart, index, rtext.lstrip()

text = "In 2005, Halton Borough Council put up a notice to tell the public about its plans to move a path from one place to another."
words = text.split(" ")
segment_words = list(zip(range(5,5+10*len(words),10),range(10,10+10*len(words),10),words))

splitted_text_w_times = []
rtext = text
index = 0
while len(rtext) > 42:
    ltext, rstart, index, rtext = smart_split(rtext, segment_words, index)
    splitted_text_w_times.extend([ltext, rstart])
splitted_text_w_times.append(rtext)
print(segment_words)
print(splitted_text_w_times)

start_list = []
end_list = []
text_list = []
start_list.append(segment_words[0][0])
text_list.append(splitted_text_w_times.pop(0))
while len(splitted_text_w_times) > 0:
    time = splitted_text_w_times.pop(0)
    end_list.append(time)
    start_list.append(time)
    text_list.append(splitted_text_w_times.pop(0))
end_list.append(segment_words[-1][1])
print(list(zip(start_list, end_list, text_list)))


