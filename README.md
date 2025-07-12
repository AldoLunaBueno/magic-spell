# MagicSpell: Herramienta de Subtítulos Educativos Bilingües

**MagicSpell** es una herramienta de línea de comandos desarrollada en Python que permite subtitular automáticamente videos en **inglés** y su respectiva traducción al **español** (u otro idioma configurable). Esta herramienta está pensada especialmente con fines educativos, facilitando la comprensión audiovisual mediante subtítulos bilingües sincronizados.

---

## Características

- Acepta archivos de video como entrada (`.mp4`, `.mkv`, etc.)
- Transcribe el audio con modelos de **Faster-Whisper**
- Traduce el texto transcrito a otro idioma (por defecto, español)
- Genera subtítulos en ambos idiomas (formato `.srt`)
- Soporte para palabras clave o difíciles ("hotwords")
- Límite de caracteres por línea de subtítulo
- Inserta los subtítulos en el video final

---

## Requisitos

- Python 3.8 o superior
- ffmpeg (instalado y accesible desde la terminal)

Instalación de dependencias:

```bash
pip install -r requirements.txt
```

> Asegúrate de haber descargado previamente los modelos de Faster-Whisper si no se descargan automáticamente.

## Uso

```bash
python main.py <ruta/al/video> [opciones]
```

### Argumentos
- input_file: Ruta del archivo de video a procesar.


### Opciones
| Opción                | Descripción                                                                         | Valor por defecto |
| --------------------- | ----------------------------------------------------------------------------------- | ----------------- |
| `--trans_lang, -l`    | Idioma al que se traducirá el texto (por ejemplo: `es`, `fr`, `pt`)                 | `es`              |
| `--hotwords_file, -w` | Ruta al archivo con palabras clave o difíciles (separadas por espacio)              | `None`            |
| `--line_limit, -L`    | Límite máximo de caracteres por línea de subtítulo                                  | `44`              |
| `--model, -m`         | Modelo de Faster-Whisper: `tiny`, `tiny.en`, `distil-small.en`, `small.en`, `small` | `small` (`s`)     |

## Ejemplo de uso

```bash
python main.py example_video.mp4 -l es -w hotwords.txt -L 42 -m t
```

## Estructura del proyecto

```txt
project/
│
├── main.py               # Script principal (CLI)
├── extrac_audio.py       # Extrae el audio del video
├── transcriber.py        # Transcribe el audio (Faster-Whisper)
├── translator.py         # Traduce los textos
├── formater.py           # Aplica formato a los subtítulos
├── srt_maker.py          # Genera archivos SRT
├── subtitle_loader.py    # Inserta los subtítulos en el video
├── requirements.txt      # Dependencias del proyecto

```
