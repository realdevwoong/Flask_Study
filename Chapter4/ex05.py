# 2. 라우팅과 HTTP 메서드
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/user/<username>')
def show_user_profile(username):
    return f'User: {username}'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return f'Post ID: {post_id}'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return 'POST 요청으로 로그인 처리'
    else:
        return 'GET 요청으로 로그인 폼 표시'

if __name__ == '__main__':
    app.run(debug=True)