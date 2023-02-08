#https://www.youtube.com/watch?v=bzbrpkbjWe8&t=981sで勉強
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello World!" 


@app.route("/")
def hello_world():
    return "Hello World!" 