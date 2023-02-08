#https://www.youtube.com/watch?v=bzbrpkbjWe8&t=981sで勉強
from flask import Flask

app = Flask(__name__)

#ルーティング
#可変のURL
@app.route("/japan/<city>") #cityを変数に
def japan(city): #cityを引数に
    return f"Hello, { city } in Japan!" 



