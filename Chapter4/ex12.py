from flask import Flask, render_template

app = Flask(__name__)

@app.route("/filter")
def filter_example():
    return render_template("filter.html", name="Programming")

if __name__ == "__main__":
    app.run(debug=True)
