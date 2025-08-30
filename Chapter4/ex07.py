#pip show Jinja2
#pip install Jinja2
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/form", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        name = request.form.get("name")
        return f"안녕하세요, {name} 님!"
    return render_template("form.html")

if __name__ == "__main__":
    app.run(debug=True)