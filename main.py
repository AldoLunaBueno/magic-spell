import click
import extrac_audio as audio
import transcriber
import translator
import subtitle_loader as subloader
import srt_maker
import splitter
import formater
from faster_whisper.transcribe import Segment, Word

@click.command()
@click.argument("input_file")
@click.option("--output_lang", "-o", default="es", help="The output language.")

def main(input_file: str, output_lang: str, temp_audio: str = "audio.aac"):
    path, slash, input_file = input_file.rpartition("\\") # Windows
    path, slash, input_file = input_file.rpartition("/") # Linux

    name, dot, extension = input_file.rpartition(".")
    output_file_name = f"{name}_with_subtitles"
    output_file = f"{name}_with_subtitles.{extension}"

    audio.extract_audio(input_file, temp_audio)
    s_list, e_list, t_list, words_list, language = transcriber.transcribe(input_file, temp_audio)
    trans_text_list = translator.translate(t_list)
    lines = s_list, e_list, t_list, words_list
    s_list, e_list, t_list, trans_text_list = formater.format(lines, trans_text_list, 44)
    lines = s_list, e_list, t_list
    translated_lines = s_list, e_list, trans_text_list
    en_srt = srt_maker.to_srt(lines, "en", output_file_name)
    es_srt = srt_maker.to_srt(translated_lines, "es", output_file_name)
    subloader.load(input_file, en_srt, es_srt, output_file)

if __name__=="__main__":
    main()