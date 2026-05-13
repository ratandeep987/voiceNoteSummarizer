# AI Voice Note Summarizer

An AI-powered web application that converts voice notes into text and generates concise summaries using speech recognition and Natural Language Processing (NLP).

## Features

* Upload voice/audio files
* Convert speech to text using Whisper AI
* Generate short AI-based summaries
* Simple and responsive user interface
* Fast processing with Flask backend

## Tech Stack

### Frontend

* HTML
* CSS
* JavaScript

### Backend

* Python
* Flask

### AI / NLP

* OpenAI Whisper
* Transformers

## Project Structure

```bash
voice-note-summarizer/
│
├── app.py
├── requirements.txt
├── uploads/
├── services/
│   ├── transcriber.py
│   └── summarizer.py
├── templates/
│   └── index.html
└── static/
```

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/ratandeep987/voiceNoteSummarizer.git
cd voiceNoteSummarizer
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

### 3. Activate Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Mac/Linux

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the Application

```bash
python app.py
```

## How It Works

1. User uploads a voice note.
2. Whisper AI converts audio into text.
3. The summarizer processes the transcript.
4. A concise summary is displayed to the user.

## Future Improvements

* Support multiple languages
* Add authentication system
* Deploy on cloud platforms
* Real-time voice recording support
* Export summaries as PDF

## Author

### Ratan Deep

* GitHub: [https://github.com/ratandeep987](https://github.com/ratandeep987)
* LinkedIn: [https://www.linkedin.com](https://www.linkedin.com/in/ratan987)

## License

This project is developed for learning and educational purposes.
