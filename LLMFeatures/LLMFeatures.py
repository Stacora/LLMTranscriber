from pathlib import Path
from typing import Union
from pydub import AudioSegment
from IPython.display import Markdown, display, update_display
import tempfile
import io

## Transcrition Function
def handle_audio_input(audio, model):
    """Transcribe audio input using Whisper"""
    if audio is None:
        return ""
    
    try:
        audio_file = open(audio, "rb")
        transcript = model.audio.transcriptions.create(
            model="whisper-1",
            file=audio_file
        )
        return transcript.text
    except Exception as e:
        return f"Error transcribing audio: {str(e)}"


## Transcript all scripts
def transcript_all(listAudios, model):
    transcripts = {}
    whole_script = ''
    for i in listAudios:
        transcript_text = handle_audio_input(str(i), model)
        transcripts['part1'] = {'path' : i,
                            'transcript' : transcript_text}
        
        whole_script += transcript_text
        
    return whole_script, transcripts