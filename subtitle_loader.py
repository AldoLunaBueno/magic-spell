import ffmpeg

input_file = "eng_cut_input.mkv"
subtitle_file = "subtitle.ass"
name, dot, extension = input_file.rpartition(".")
output_file = f"{name}_with_subtitle.{extension}"

input = ffmpeg.input(input_file)
video_with_subs = input.filter(
        "subtitles", 
        subtitle_file,
        force_style="Name:Español,FontName=Arial,FontSize=18,PrimaryColour=&H0000FCFF,OutlineColour=&H00000000&,BackColour=&H00000000&,MarginV=20"
    ).filter(
        "subtitles", 
        subtitle_file,
        force_style="Name:English,FontName=Consolas,FontSize=22,PrimaryColour=&H00FFFFFF,OutlineColour=&H00000000&,BackColour=&H00000000&,BorderStyle=1,Outline=3.5,Shadow=1.5,Alignment=2,MarginV=0"
    )

(
    ffmpeg
    .output(
        video_with_subs, 
        input.audio, 
        output_file,
        preset='ultrafast', 
        tune='zerolatency',  # Reduces latency
        acodec="copy")
    .run(overwrite_output=True)
)