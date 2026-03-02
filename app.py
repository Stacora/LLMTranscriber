import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os
from pathlib import Path
from pydub import AudioSegment
from IPython.display import Markdown, display, update_display

## audio tools
from AudioTools.audio_tools import convert_to_mp3

st.markdown("# Summarize meetings")

col1_setings, col2_output = st.columns([6, 8])

with col1_setings:
    audio_filename = st.file_uploader(label = "Upload audio file:")
    
    if audio_filename:
        out_dir = Path("Audios/converted") ## Here the audios will be saved
        filename = Path(audio_filename.name).stem
        
        convert_to_mp3(input_audio = audio_filename,
                       out_dir = out_dir,
                       filename = filename)
        
        
    
with col2_output:
    st.write("Here come the output")