from flask import Flask, render_template

app = Flask(__name__)


@app.route("/status")
def status():
    return render_template("status.html", is_login=False)

if __name__ == "__main__":
    app.run(debug=True)