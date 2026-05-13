from groq import Groq

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def transcribe(audio_file_path):
    with open(audio_file_path, "rb") as file:
        transcription = client.audio.transcriptions.create(
            file=(audio_file_path, file.read()),
            model="whisper-large-v3"
        )
    return transcription.text