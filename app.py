from flask import Flask
#from flask_restful import Api
#from bq import bq


app = Flask(__name__)

@app.route("/")
def home():
    return '{"hello" : "world"}'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)