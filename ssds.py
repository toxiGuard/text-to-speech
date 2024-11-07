import simpleaudio as sa
from pydub import AudioSegment
from io import BytesIO
from pymongo import MongoClient
from bson import Binary
import os

mongo_uri = os.getenv("MONGO_URI")
client = MongoClient("mongodb+srv://shyamal116:bstisdcan1S@cluster0.8awyqnb.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client["test"]
collection = db["test"]

def fetch_and_play_audio(audio_id):
    # Fetch the audio data from MongoDB
    document = collection.find_one({"name": audio_id})
    
    if not document:
        print(f"No audio found for ID {audio_id}.")
        return
    
    # Extract the audio binary data from MongoDB document
    audio_binary = document.get("audio_data")
    
    if not audio_binary:
        print(f"No audio data found for ID {audio_id}.")
        return

    # Convert the binary data back to an AudioSegment object
    audio_stream = BytesIO(audio_binary)
    audio_segment = AudioSegment.from_file(audio_stream, format="mp3")  # Assuming it's stored as MP3 in MongoDB
    
    # Convert audio to raw audio format (like WAV) for playback
    raw_audio = audio_segment.raw_data
    
    # Play the audio using simpleaudio
    play_obj = sa.play_buffer(raw_audio, num_channels=audio_segment.channels, 
                              bytes_per_sample=audio_segment.sample_width, 
                              sample_rate=audio_segment.frame_rate)
    play_obj.wait_done()

# Example usage
audio_id = "f44d6bb1-d677-430e-861d-0ed6fccb266a"  # Replace with your actual ID stored in MongoDB
fetch_and_play_audio(audio_id)
