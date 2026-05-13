from flask import Flask, request, jsonify, render_template
import os

from services.transcriber import transcribe_audio
from services.summarizer import summarize_text

from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload_audio():

    if "audio" not in request.files:
        return jsonify({"error": "No file uploaded"})

    audio = request.files["audio"]

    file_path = os.path.join(UPLOAD_FOLDER, audio.filename)

    audio.save(file_path)

    transcription = transcribe_audio(file_path)

    summary = summarize_text(transcription)

    return jsonify({
        "transcription": transcription,
        "summary": summary
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)