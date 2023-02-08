#https://www.youtube.com/watch?v=bzbrpkbjWe8&t=981sで勉強
from flask import Flask
from flask import render_template
app = Flask(__name__)

#テンプレートを用いる
@app.route("/japan/<city>") 
def hello(city): 
    return render_template("hello.html", city=city) #左はhello.htmlで使うcity、右のcityは引数として用いられるcity





