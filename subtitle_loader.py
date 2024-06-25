import ffmpeg

input_lang_style = "Name:InputLang,FontName=Consolas,FontSize=22,PrimaryColour=&H00FFFFFF,OutlineColour=&H00000000&,BackColour=&H00000000&,BorderStyle=1,Outline=1.5,Shadow=0.5,Alignment=2,MarginV=0"
output_lang_style = "Name:OutputLang,FontName=Arial,FontSize=18,PrimaryColour=&H0000FCFF,OutlineColour=&H00000000&,BackColour=&H00000000&,MarginV=20"

def load(input_file, input_subtitle_file, output_subtitle_file, output_file):

    input = ffmpeg.input(input_file)
    video_with_subs = input.filter(
            "subtitles", 
            output_subtitle_file,
            force_style=output_lang_style
        ).filter(
            "subtitles", 
            input_subtitle_file,
            force_style=input_lang_style
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