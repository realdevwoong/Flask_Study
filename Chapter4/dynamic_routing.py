from flask import Flask

app = Flask(__name__)
#동적 라우팅 
@app.route("/")
def home():
    return "hello Flask!"

@app.route("/user/<username>")
def profile(username):
    return f"User: {username}"

@app.route("/post/<int:post_id>")
def show_post(post_id):
    return f"Post ID: {post_id}"
  
if __name__ == "__main__":
    app.run( 
      host="127.0.0.1",
      port=5000,
      debug=True
)