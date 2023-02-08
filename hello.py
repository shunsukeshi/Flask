#https://www.youtube.com/watch?v=bzbrpkbjWe8&t=981sで勉強
from flask import Flask

app = Flask(__name__)

html = ''' #文字列としてhtmlを記載
<h1>サンプルHTML<h1>
<ul>
    <li>箇条書き1</li>
    <li>箇条書き2</li>
    <li>箇条書き3</li>
</ul>
'''

#HTMLを書いてみる
@app.route("/") 
def hello(): 
    return html #returnでhtml呼ぶ

#pythonの中にHTMLを書くのはあまり良くない...→テンプレートを使う



