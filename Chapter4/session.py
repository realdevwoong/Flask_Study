import os
from flask import Flask, session
# from dotenv import load_dotenv
# load_dotenv()  

app = Flask(__name__)
app.secret_key = os.urandom(24) 
#app.secret_key = os.getenv("SECRET_KEY")
@app.route("/set_session")
def set_session():
    session["username"] = "woong"
    return "세션 설정 완료"
print(app.secret_key)

@app.route("/get_session")
def get_session():
    return f"세션 값: {session.get('username')}"

#pip install python-dotenv

if __name__ == "__main__":
    app.run(debug=True)