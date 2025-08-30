from flask import Flask, render_template
from datetime import date

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("hello.html", username="woong", today=date.today())

if __name__ == "__main__":
    app.run(debug=True)