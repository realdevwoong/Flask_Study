import logging
from flask import Flask
app = Flask(__name__)
logging.getLogger('werkzeug').setLevel(logging.ERROR)
@app.route("/")       
def home():
    return "Hello, Flask!"

@app.route("/about")  
def about():
    return "About Page"

if __name__ == "__main__":
    app.run(
        debug=True,
        host="0.0.0.0",
        port=5001
    )
#flask run --debug --host=0.0.0.0 --port=5001
