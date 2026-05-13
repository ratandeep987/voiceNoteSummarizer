from groq import Groq

client = Groq(
    api_key="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"
)

def summarize_text(text):
    response = client.chat.completions.create(
       model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": f"Summarize this voice note:\n{text}"
            }
        ]
    )

    return response.choices[0].message.content