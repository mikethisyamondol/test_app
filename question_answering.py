from transformers import AutoTokenizer,AutoModelForQuestionAnswering
import torch


# def qna():
#     model_name = "deepset/roberta-base-squad2"
#     nlp = pipeline('question-answering', model=model_name, tokenizer=model_name)

#     result = nlp(input)
#     return result 

def qna(question, context):
	#model and tokeniser from Hugging face
	tokenizer =  AutoTokenizer.from_pretrained('deepset/bert-base-cased-squad2')
	model = AutoModelForQuestionAnswering.from_pretrained('deepset/bert-base-cased-squad2')

	#Use model 'ponmari/QuestionAnsweingBert'

	
	input_ids = tokeniser.encode(question, context)
	
	sep_index = input_ids.index(tokenizer.sep_token_id)

	num_seg_a = sep_index+1
	num_seg_b = len(input_ids) - num_seg_a

	segment_ids = [0]*num_seg_a + [1]*num_seg_b

	assert len(segment_ids) == len(input_ids)

	#Running the model with input
	start_scores,end_scores = model(torch.tensor([input_ids]),token_type_ids=torch.tensor([segment_ids]))

	answer_start = torch.argmax(start_scores)
	answer_end = torch.argmax(end_scores)

	answer = ' '.join(tokens[answer_start:answer_end+1])
	print(answer)
	return {'Answer':answer}

