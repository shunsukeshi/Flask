#https://www.youtube.com/watch?v=bzbrpkbjWe8&t=981sで勉強
from flask import Flask
from flask import render_template
app = Flask(__name__)

bullets = [
    "箇条書き1",
    "箇条書き2",
    "箇条書き3",
    "箇条書き4",
    "箇条書き5",
    "箇条書き6",
    "箇条書き7",
    "箇条書き8",
]

#テンプレートを用いる
@app.route("/") 
def hello(): 
    return render_template("hello.html", bullets=bullets)





