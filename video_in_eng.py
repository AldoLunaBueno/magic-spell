import ffmpeg

def get_audio_stream_index_by_language(input_file, language_code):
    # Obtener la información de los streams
    probe = ffmpeg.probe(input_file)
    audio_streams = [stream for stream in probe['streams'] if stream['codec_type'] == 'audio']

    # Buscar el índice del stream que tiene el idioma deseado
    for stream in audio_streams:
        if 'tags' in stream and 'language' in stream['tags'] and stream['tags']['language'] == language_code:
            return stream['index']
    return None

input_file = "cut_input.mkv"
language_code = "eng"
audio_codec = "acc"
name, dot, extension = input_file.rpartition(".")
output_file = f"{language_code}_{name}.{extension}"


# Obtener el índice del stream de audio en inglés
audio_stream_index = get_audio_stream_index_by_language(input_file, language_code)

if audio_stream_index is None:
    print(f"No se encontró una pista de audio con el idioma {language_code}")

# Extraer la pista de audio en inglés usando el índice encontrado

input = ffmpeg.input(input_file)
(
    ffmpeg
    .output(
        input.video,
        output_file,
        vcodec="copy",
        acodec="aac",
        map=f"0:{audio_stream_index}")
    .run(quiet=True, overwrite_output=True)  
)