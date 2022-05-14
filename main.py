# from flask import Flask, request, jsonify
# from flask_restful import Api
# from bq import bq
from question_answering import qna
from fastapi import FastAPI
import uvicorn


app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome"}

@app.get("/answer/{question}/{context}")
async def answer(question: str, context: str):
    return qna(question, context)

if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='0.0.0.0')