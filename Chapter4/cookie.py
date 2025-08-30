from flask import Flask, request, make_response

app = Flask(__name__)

@app.route("/set_cookie")
def set_cookie():
    resp = make_response("쿠키 설정 완료")
    resp.set_cookie("username", "woong", max_age=10)  # 5분 동안 유지
    return resp

@app.route("/get_cookie")
def get_cookie():
    username = request.cookies.get("username")
    return f"쿠키 값: {username}"

if __name__ == "__main__":
    app.run(debug=True)