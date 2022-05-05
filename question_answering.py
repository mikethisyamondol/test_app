from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline


def qna(input):
    model_name = "deepset/roberta-base-squad2"
    nlp = pipeline('question-answering', model=model_name, tokenizer=model_name)

    result = nlp(input)
    return result 

