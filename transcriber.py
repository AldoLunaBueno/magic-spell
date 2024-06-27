from typing import List, Tuple, Iterable
from faster_whisper import WhisperModel
from faster_whisper.transcribe import Word

# tiny distil-small.en small.en 
model_size = "small"

def transcribe(input_file: str, hotwords_file: str, audio_file: str) -> Tuple[Tuple[List[float], List[float], List[str], List[List[Word]]], str]:

    name, dot, _ = input_file.rpartition(".")
    srt_file = f"{name}_with_subtitles.srt" 

    model = WhisperModel(model_size, device="cpu", compute_type="int8", cpu_threads=6)

    # Opciones de transcripción
    language = "en"

    hotwords = ""
    with open(hotwords_file, "r") as f:
        hotwords = " ".join([line.strip() for line in f.readlines()])
    options = dict(
        beam_size = 3,
        length_penalty = 0.2,
        hotwords = hotwords,
        vad_filter = False,
        #vad_parameters = dict(min_silence_duration_ms=1500),
        hallucination_silence_threshold = 0.2,
        language = language,
        word_timestamps=True,
        )
    segments, info = model.transcribe(audio_file, **options)
    start_list = []
    end_list = []
    text_list = []
    words_list = []
    for segment in segments:
        start_list.append(segment.start)
        end_list.append(segment.end)
        text_list.append(segment.text)
        words_list.append(segment.words)
    language = info[0]
    return start_list, end_list, text_list, words_list, language