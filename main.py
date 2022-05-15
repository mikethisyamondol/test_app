# from question_answering import qna
from fastapi import FastAPI
import uvicorn
from transformers import pipeline


app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome"}

@app.get("/answer/{question}/{context}")
async def answer(question: str, context: str):
    model_name = "deepset/roberta-base-squad2"
    nlp = pipeline('question-answering', model=model_name, tokenizer=model_name)
    qa_input = {'question': question, 'context': context}
    result = nlp(qa_input)
    return {'Answer': result}
    # return qna(question, context)

if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='0.0.0.0')