import whisper

model = whisper.load_model("tiny")

def transcribe_audio(file_path):
    result = model.transcribe(
        file_path,
        fp16=False,
        beam_size=1,
        best_of=1,
        condition_on_previous_text=False,
        verbose=False
    )

    return result["text"]