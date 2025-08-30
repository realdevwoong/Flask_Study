#기본 플라스크 
from flask import Flask
app = Flask(__name__)
#앱의 시작점 
@app.route("/")       
def home():
    return "Hello, Flask!"

@app.route("/about")  
def about():
    return "About Page"

if __name__ == "__main__":
    app.run()