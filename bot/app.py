from fastapi import FastAPI
from pydantic import BaseModel
import os
import openai

class Question(BaseModel):
    text: str

app = FastAPI()

# Load OpenAI API key from environment
openai.api_key = os.environ.get("OPENAI_API_KEY")

@app.post("/ask")
def ask(question: Question):
    """Return answer from OpenAI's chat completion API."""
    if not openai.api_key:
        return {"error": "OPENAI_API_KEY not set"}
    messages = [
        {"role": "system", "content": "You are a study assistant for the IPA Information Security Management Exam."},
        {"role": "user", "content": question.text},
    ]
    try:
        response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
        answer = response.choices[0].message.content
    except Exception as e:
        return {"error": str(e)}
    return {"answer": answer}
