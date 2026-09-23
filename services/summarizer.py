import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv() 

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def summarize_text(text):
    response = client.chat.completions.create(
    model="openai/gpt-oss-20b",
        messages=[
            {
                "role": "user",
                "content": f"Summarize this voice note:\n{text}"
            }
        ]
    )

    return response.choices[0].message.content