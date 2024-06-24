from faster_whisper import WhisperModel
# tiny distil-small.en small.en 
model_size = "small"
model = WhisperModel(model_size, device="cpu", compute_type="int8", cpu_threads=6)
audio_file = "audio.aac"
audio_name, dot, extension = audio_file.rpartition(".")
srt_file = f"{audio_name}.srt"

# Opciones de transcripción
language = "en"
hotwords = "Asta Wizard King grimoire"
prompt = "In a world where magic is everything, Asta and Yuno are two orphans raised together with the dream of becoming the Wizard King, the most powerful protector of the kingdom."
options = dict(
    beam_size = 2,
    length_penalty = 0.5,
    hotwords = hotwords,
    vad_filter = True,
    vad_parameters = dict(min_silence_duration_ms=1500),
    hallucination_silence_threshold = 0.2,
    language = language,
    word_timestamps=True,
)

def srt_time(seconds: int) -> str:
    mm = int(seconds) // 60
    ss = seconds - 60 * mm
    hh = mm // 60
    mm -= 60*hh
    return f"{hh:02}:{mm:02}:{ss:06,.3f}".replace('.',',')

segments, info = model.transcribe(audio_file, **options)
srt_content = []
for index, segment in enumerate(segments, 1):
    start_time = srt_time(segment.start)
    end_time = srt_time(segment.end)
    str_entry = f"{index}\n{start_time} --> {end_time}\n{segment.text.strip()}\n"
    srt_content.append(str_entry)
    # for word in segment.words:
    #     print(f"Word: {word.word}, Start: {word.start}, End: {word.end}")

srt_content = "\n".join(srt_content)

with open(srt_file, "w", encoding="utf-8") as f:
    f.write(srt_content)

