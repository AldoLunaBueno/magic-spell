import click
import extrac_audio as audio
import transcript
import translate
import subtitle_loader as subloader
import srt_maker

@click.command()
@click.argument("input_file")
@click.option("--output_lang", "-o", default="es", help="The output language.")

def main(input_file: str, output_lang: str, temp_audio: str = "audio.aac"):
    path, slash, input_file = input_file.rpartition("\\") # Windows
    path, slash, input_file = input_file.rpartition("/") # Linux

    name, dot, extension = input_file.rpartition(".")
    output_file_name = f"{name}_with_subtitles"
    output_file = f"{name}_with_subtitles.{extension}"

    #audio.extract_audio(input_file, temp_audio)
    lines, language = transcript.transcribe(input_file, temp_audio)
    text = lines[2]
    translated = translate.translate(text)
    en_srt = srt_maker.to_srt((lines[0], lines[1], text), "en", output_file_name)
    #es_srt = srt_maker.to_srt((lines[0], lines[1], translated), "es", output_file_name)
    #subloader.load(input_file, en_srt, es_srt, output_file)

if __name__=="__main__":
    main()