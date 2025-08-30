from flask import Flask, render_template

app = Flask(__name__)

@app.route("/programming")
def programming():
    languages = ["Python", "JavaScript", "C++", "Java", "Go"]
    return render_template("programming.html", languages=languages)

if __name__ == "__main__":
    app.run(debug=True)