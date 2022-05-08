# from flask import Flask, request, jsonify
# from flask_restful import Api
# from bq import bq
from question_answering import qna
from fastapi import FastAPI
import uvicorn


# app = Flask(__name__)
# api = Api(app)

# query = '''
# with double_entry_book as (
#     -- debits
#     select to_address as address, value as value
#     from `bigquery-public-data.crypto_ethereum.traces`
#     where to_address is not null
#     and status = 1
#     and (call_type not in ('delegatecall', 'callcode', 'staticcall') or call_type is null)
#     union all
#     -- credits
#     select from_address as address, -value as value
#     from `bigquery-public-data.crypto_ethereum.traces`
#     where from_address is not null
#     and status = 1
#     and (call_type not in ('delegatecall', 'callcode', 'staticcall') or call_type is null)
#     union all
#     -- transaction fees debits
#     select 
#         miner as address, 
#         sum(cast(receipt_gas_used as numeric) * cast((receipt_effective_gas_price - coalesce(base_fee_per_gas, 0)) as numeric)) as value
#     from `bigquery-public-data.crypto_ethereum.transactions` as transactions
#     join `bigquery-public-data.crypto_ethereum.blocks` as blocks on blocks.number = transactions.block_number
#     group by blocks.number, blocks.miner
#     union all
#     -- transaction fees credits
#     select 
#         from_address as address, 
#         -(cast(receipt_gas_used as numeric) * cast(receipt_effective_gas_price as numeric)) as value
#     from `bigquery-public-data.crypto_ethereum.transactions`
# )
# select address, sum(value) as balance
# from double_entry_book
# group by address
# order by balance desc
# limit 100;
# '''

# @app.route("/", methods=['GET', 'POST'])
# def home():
#     # if request.method == 'GET':
#     inputs = request.get_json()
#     question = inputs['question']
#     context   = inputs['context']

#     return jsonify(qna(question, context))


# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=8080, debug=True)

app = FastAPI()

@app.get("/{question}/{context}")
async def root(question: str, context: str):
    return qna(question, context)

if __name__ == '__main__':
    # uvicorn.run(app, port=8080, host='0.0.0.0')
    app.run(host="0.0.0.0", port=8080, debug=True)