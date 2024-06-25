import ffmpeg

def extract_audio(input_file, temp_audio, language_code="eng"):
    # Obtener el índice del stream de audio en inglés
    audio_stream_index = __get_audio_stream_index_by_language__(input_file, language_code)

    if audio_stream_index is None:
        print(f"No se encontró una pista de audio con el idioma {language_code}")

    # Extraer la pista de audio en inglés usando el índice encontrado

    (
        ffmpeg
        .input(input_file)
        .output(
            temp_audio,
            map=f"0:{audio_stream_index}"
        ).run(overwrite_output=True)  
    )

def __get_audio_stream_index_by_language__(input_file, language_code):
    # Obtener la información de los streams
    probe = ffmpeg.probe(input_file)
    audio_streams = [stream for stream in probe['streams'] if stream['codec_type'] == 'audio']

    # Buscar el índice del stream que tiene el idioma deseado
    for stream in audio_streams:
        if 'tags' in stream and 'language' in stream['tags'] and stream['tags']['language'] == language_code:
            return stream['index']
    return None