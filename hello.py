#https://www.youtube.com/watch?v=bzbrpkbjWe8&t=981sで勉強
from flask import Flask

app = Flask(__name__)

#ルーティングの実施
@app.route("/japan")
def japan():
    return "Hello Japan!" 

@app.route("/america")
def america():
    return "Hello America!" 

@app.route("/world")
def world():
    return "Hello World!" 