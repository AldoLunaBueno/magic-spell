from typing import List, Tuple, Iterable
from faster_whisper import WhisperModel
from faster_whisper.transcribe import Segment

# tiny distil-small.en small.en 
model_size = "small"

def transcribe(input_file, audio_file) -> Tuple[Tuple[List[float], List[float], List[str]], str]:

    name, dot, _ = input_file.rpartition(".")
    srt_file = f"{name}_with_subtitles.srt" 

    model = WhisperModel(model_size, device="cpu", compute_type="int8", cpu_threads=6)

    # Opciones de transcripción
    language = "en"
    hotwords = "Asta Wizard King grimoire Yuno Hage Yami Sukehiro Luck Noelle Nozel Secre Mimosa Marie William Vangeance Mereoleona Julius Novachrono Sekke Bronzazza"
    options = dict(
        beam_size = 2,
        length_penalty = 0.3,
        hotwords = hotwords,
        vad_filter = True,
        vad_parameters = dict(min_silence_duration_ms=1500),
        hallucination_silence_threshold = 0.2,
        language = language,
        word_timestamps=True,
        )
    segments, info = model.transcribe(audio_file, **options)
    language = info[0]
    return __process__(segments), language

def __process__(segments: Iterable[Segment]) -> Tuple[List[float], List[float], List[str]]:
    start = []
    end = []
    text = []

    for segment in segments:
        start.append(segment.start)
        end.append(segment.end)
        text.append(segment.text)
        
    return start, end, text