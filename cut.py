import ffmpeg

input_file = "input.mkv"
name, dot, extension = input_file.rpartition(".")
output_file = f"cut_{name}.{extension}"
start_time = "00:17:24"
end_time = "00:18:24"

# Usando ffmpeg-python para cortar el video y mantener todas las pistas
ffmpeg.input(input_file, ss=start_time, to=end_time).output(output_file, map='0', c='copy').run(quiet=True)