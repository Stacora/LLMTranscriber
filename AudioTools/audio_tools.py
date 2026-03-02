from pathlib import Path
from typing import Union
from pydub import AudioSegment
from IPython.display import Markdown, display, update_display
import tempfile
import io


def convert_to_mp3_flexStr(
    input_audio: Union[Path, io.BytesIO],
    out_dir: Path,
    filename
) -> Path:
    """
    Converts audio to MP3.
    
    - input_audio: Path OR file-like object (e.g. Streamlit UploadedFile)
    - out_dir: directory where the mp3 will be saved
    - filename: required if input_audio is not a Path
    """

    out_dir.mkdir(parents=True, exist_ok=True)

    # Case 1: input is a Path
    if isinstance(input_audio, Path):
        mp3_path = out_dir / f"{input_audio.stem}.mp3"
        audio = AudioSegment.from_file(str(input_audio))

    # Case 2: input is an UploadedFile / BytesIO
    else:
        if filename is None:
            raise ValueError("filename is required when input_audio is not a Path")

        mp3_path = out_dir / f"{Path(filename).stem}.mp3"

        audio = AudioSegment.from_file(
            input_audio,
            format=Path(filename).suffix.replace(".", "")
        )

    audio.export(str(mp3_path), format="mp3", bitrate="64k")
    return mp3_path

def convert_to_mp3(input_path: Path, out_dir: Path) -> Path:
    """
    Convert audio to MP3 using pydub (requires ffmpeg installed).
    input_path: path of the file to convert
    outdir: Path where you want to store the final result
    """

    out_dir.mkdir(parents=True, exist_ok=True)
    mp3_path = out_dir / f"{input_path.stem}.mp3"

    audio = AudioSegment.from_file(str(input_path))
    audio.export(str(mp3_path), format="mp3")

    return mp3_path

def split_audio_with_overlap(input_path, chunk_ms, overlap_ms):
    audio = AudioSegment.from_file(input_path)
    chunks = []
    step = chunk_ms - overlap_ms

    for i in range(0, len(audio), step):
        chunk = audio[i:i + chunk_ms]
        out = Path(input_path).with_suffix(f".part{i//step}.mp3")
        chunk.export(out, format="mp3")
        chunks.append(out)

    return chunks
