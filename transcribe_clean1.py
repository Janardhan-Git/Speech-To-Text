import whisper
import datetime
import re

# Load Whisper model
model = whisper.load_model("tiny")  # Change to "base", "small", etc. as needed

# Transcribe your audio
audio_path = "CapGemini_audio.mp3"
result = model.transcribe(audio_path)

# Format time
def format_time(seconds):
    return str(datetime.timedelta(seconds=int(seconds)))

# Clean and split text after full stops
def split_and_format(text):
    return re.split(r'(?<=[.?!])\s+', text.strip())

# Open file to write

with open("transcript.txt", "w", encoding="utf-8") as f:
    for seg in result["segments"]:
        start = format_time(seg["start"])
        end = format_time(seg["end"])
        text = seg["text"].strip()
        
        speaker = "Interviewer" if "?" in text or text.lower().startswith((
            "can you", "what", "how", "tell me", 
            "do you", "did you", "why", "please", 
            "explain", "have you", "could you"
        )) else "Candidate"
        
        for line in split_and_format(text):
            formatted_line = f"[{start} - {end}] {speaker}: {line}\n"
            print(formatted_line.strip())  # Optional: still see output in console
            f.write(formatted_line)

'''
with open("transcript.txt", "w", encoding="utf-8") as f:
    for seg in result["segments"]:
        start = format_time(seg["start"])
        end = format_time(seg["end"])
        text = seg["text"].strip()
        
        speaker = "Interviewer" if "?" in text or text.lower().startswith((
            "can you", "what", "how", "tell me", 
            "do you", "did you", "why", "please", 
            "explain", "have you", "could you"
        )) else "Candidate"
        
        for line in split_and_format(text):
            formatted_line = f"[{start} - {end}] {speaker}: {line}\n"
            print(formatted_line.strip())  # Optional: still see output in console
            f.write(formatted_line)
