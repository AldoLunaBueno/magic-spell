import ffmpeg

input_file = "eng_cut_input.mkv"
subtitle_file_1 = "eng_cut_input.es.srt"
subtitle_file_2 = "eng_cut_input.srt"
spanish_style = "Name:Spanish,FontName=Arial,FontSize=18,PrimaryColour=&H0000FCFF,OutlineColour=&H00000000&,BackColour=&H00000000&,MarginV=20"
english_style = "Name:English,FontName=Consolas,FontSize=22,PrimaryColour=&H00FFFFFF,OutlineColour=&H00000000&,BackColour=&H00000000&,BorderStyle=1,Outline=1.5,Shadow=0.5,Alignment=2,MarginV=0"
name, dot, extension = input_file.rpartition(".")
output_file = f"{name}_with_subtitles.{extension}"

input = ffmpeg.input(input_file)
video_with_subs = input.filter(
        "subtitles", 
        subtitle_file_1,
        force_style=spanish_style
    ).filter(
        "subtitles", 
        subtitle_file_2,
        force_style=english_style
    ).filter(
        "scale", 1280, -1
    )

(
    ffmpeg
    .output(
        video_with_subs, 
        input.audio, 
        output_file,
        vcodec='libx264', # Utiliza el codec H.264 para la codificación de video.
        preset='ultrafast', # Usa el preajuste ultrafast para maximizar la velocidad de codificación
        tune='zerolatency',  # Reduce la latencia
        video_bitrate='300k',  # Usa una tasa de bits más baja, reduciendo el tamaño del archivo
        audio_bitrate='96k', # Reducir la tasa de bits del audio
        vsync='passthrough',  # Evitar verificación de duplicados
        crf=30,  # Reducir la calidad de compresión para mayor velocidad
        threads=6,
        acodec="copy"
    ).run(overwrite_output=True)
)