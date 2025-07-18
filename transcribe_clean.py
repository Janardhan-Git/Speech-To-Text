import whisper
import datetime
import re

# Load Whisper model
model = whisper.load_model("tiny")  # Change to "base", "small", etc. as needed

# Load your audio file, Transcribe your audio
audio_path = "Wipro Shanmuka Prasad Doddi.mp3"
print("⏳ Starting transcription...")
result = model.transcribe(audio_path)
print("✅ Transcription complete.")

# Helper to format seconds into hh:mm:ss
def format_time(seconds):
    return str(datetime.timedelta(seconds=int(seconds)))

# Helper to split sentences after punctuation for easy reading
def split_and_format(text):
    return re.split(r'(?<=[.?!])\s+', text.strip())

# === 📍  PROGRESS CODE  ===

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
            
            
st.markdown("---")
st.caption("Built with ❤️ by Jana")
            
            run_block=False


# OPTION 1: Print progress manually

"""
for i, seg in enumerate(result["segments"]):
    print(f"[{i+1}/{len(result['segments'])}] Processing segment...")
    
    start = format_time(seg["start"])
    end = format_time(seg["end"])
    text = seg["text"].strip()

    speaker = "Interviewer" if "?" in text or text.lower().startswith((
        "can you", "what", "how", "tell me", 
        "do you", "did you", "why", "please", 
        "explain", "have you", "could you"
    )) else "Candidate"
    
    lines = split_and_format(text)
    for line in lines:
        print(f"[{start} - {end}] {speaker}: {line}")

"""


