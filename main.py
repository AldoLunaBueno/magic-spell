import click
import extrac_audio as audio
import transcriber
import translator
import subtitle_loader as subloader
import srt_maker
import formater
from faster_whisper.transcribe import Segment, Word

@click.command()
@click.argument("input_file", type=str)
@click.option("--trans_lang", "-l", default="es", type=str, 
              help="The language you want the content to be translated into.")
@click.option("--hotwords_file", "-w", type=str, 
              help="File with difficult recurring words separated by spaces.")
@click.option("--line_limit", "-L", type=int,
              help="Maximum number of characters in one subtitle line.")
@click.option("--model", "-m", default="s", type=str,
              help="Choose one Faster-Whisper model: \
                tiny(t), tiny.en(te), distil-small.en(ds) small.en(se), small(s).")

def main(input_file: str, trans_lang: str, hotwords_file:str, model:str, temp_audio: str = "audio.aac", line_limit: int = 44):
    path, slash, input_file = input_file.rpartition("\\") # Windows
    path, slash, input_file = input_file.rpartition("/") # Linux

    name, dot, extension = input_file.rpartition(".")
    output_file_name = f"{name}_with_subtitles"
    output_file = f"{name}_with_subtitles.{extension}"

    audio.extract_audio(input_file, temp_audio)
    s_list, e_list, t_list, words_list, language = transcriber.transcribe(input_file, hotwords_file, temp_audio)
    trans_text_list = translator.translate(t_list)
    lines = s_list, e_list, t_list, words_list
    s_list, e_list, t_list, trans_text_list = formater.format(lines, trans_text_list, line_limit)
    lines = s_list, e_list, t_list
    translated_lines = s_list, e_list, trans_text_list
    en_srt = srt_maker.to_srt(lines, "en", output_file_name)
    es_srt = srt_maker.to_srt(translated_lines, "es", output_file_name)
    subloader.load(input_file, en_srt, es_srt, output_file)

if __name__=="__main__":
    main()