from flask import Flask, url_for, redirect

app = Flask(__name__)

@app.route('/')
def index():
    # url_for("hello", name="인웅") → /hello/인웅 으로 이동
    return redirect(url_for('hello', name='인웅'))

@app.route('/hello/<name>')
def hello(name):
    return f"안녕하세요, {name}님!"

if __name__ == "__main__":
    app.run(debug=True)