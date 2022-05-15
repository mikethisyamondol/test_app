from transformers import pipeline #AutoTokenizer,AutoModelForQuestionAnswering
# import torch


def qna(question,context):
	model_name = "deepset/roberta-base-squad2"
	nlp = pipeline('question-answering', model=model_name, tokenizer=model_name)
	input = {'question': question,
			'context': context}
	result = nlp(input)
	return {'Answer': result}