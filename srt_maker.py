from typing import List, Tuple

def to_srt(lines: Tuple[List[float], List[float], List[str]], language: str, output_file_name: str) -> str:
    """
    Generate a file with subtitles in SRT format and
    returns the name of the file.
    """
    srt_content = [f"{index}\n{__srt_time__(start)} --> {__srt_time__(end)}\n{text.lstrip()}\n" 
                   for index, (start, end, text) in enumerate(tuple(zip(*lines)), 1)]
    # for index, (start, end, text) in enumerate(tuple(zip(*lines)), 1):
    #     start = __srt_time__(start)
    #     end = __srt_time__(end)
    #     str_entry = f"{index}\n{start} --> {end}\n{text.lstrip()}\n"
    #     srt_content.append(str_entry)

    srt_content = "\n".join(srt_content)
    srt_file = f"{output_file_name}.{language}.srt"
    with open(srt_file, "w", encoding="utf-8") as f:
        f.write(srt_content)

    return srt_file

def __srt_time__(seconds: int) -> str:
        mm = int(seconds) // 60
        ss = seconds - 60 * mm
        hh = mm // 60
        mm -= 60 * hh
        return f"{hh:02}:{mm:02}:{ss:06,.3f}".replace('.',',')