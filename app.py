#https://www.youtube.com/watch?v=mW0_60SRr3s
#要素の共通化
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
