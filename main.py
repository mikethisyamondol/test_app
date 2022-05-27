from fastapi import FastAPI
import uvicorn
import requests
import os
# from transformers import pipeline
# from question_answering import qna


app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome"}

@app.get("/answer/{question}/{context}")
async def answer(question: str, context: str):
    API_URL = "https://api-inference.huggingface.co/models/deepset/roberta-base-squad2"
    headers = {"Authorization": f"Bearer {os.environ['API_KEY']}"}
    payload = {'question': question, 'context': context}
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()
   

if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='0.0.0.0')