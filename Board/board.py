from flask import Flask, render_template, request, redirect, url_for, jsonify
from datetime import datetime

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False

class Board:
    def __init__(self):
        self.posts = []
        self.seq = 0

    def next_id(self):
        self.seq += 1
        return self.seq

    def all(self):
        return sorted(self.posts, key=lambda x: x["id"])

    def get(self, pid):
        return next((p for p in self.posts if p["id"] == pid), None)

    def create(self, title, content):
        post = {
            "id": self.next_id(),
            "title": title,
            "content": content,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }
        self.posts.append(post)
        return post

    def update(self, pid, title, content):
        post = self.get(pid)
        if post:
            post["title"] = title
            post["content"] = content
        return post

    def delete(self, pid):
        before = len(self.posts)
        self.posts = [p for p in self.posts if p["id"] != pid]
        return len(self.posts) < before

# 👉 여기서 한 번만 인스턴스 생성
board = Board()

# ------------------- Flask 라우트 -------------------
@app.route("/")
def home():
    return redirect(url_for("list_posts"))

@app.route("/posts")
def list_posts():
    return render_template("index.html", posts=board.all())

@app.route("/posts/new")
def new_post():
    return render_template("form.html", mode="create", post={"title":"", "content":""})

@app.route("/posts", methods=["POST"])
def create_post():
    title = (request.form.get("title") or "").strip()
    content = (request.form.get("content") or "").strip()
    if not title or not content:
        return render_template("form.html", mode="create", post={"title":title,"content":content}, error="제목/내용은 비울 수 없습니다.")
    post = board.create(title, content)
    return redirect(url_for("show_post", post_id=post["id"]))

@app.route("/posts/<int:post_id>")
def show_post(post_id):
    post = board.get(post_id)
    if not post:
        return render_template("404.html"), 404
    return render_template("show.html", post=post)

@app.route("/posts/<int:post_id>/edit")
def edit_post(post_id):
    post = board.get(post_id)
    if not post:
        return render_template("404.html"), 404
    return render_template("form.html", mode="edit", post=post)

@app.route("/posts/<int:post_id>", methods=["POST"])
def update_post(post_id):
    title = (request.form.get("title") or "").strip()
    content = (request.form.get("content") or "").strip()
    if not title or not content:
        return render_template("form.html", mode="edit", post={"id":post_id, "title":title,"content":content}, error="제목/내용은 비울 수 없습니다.")
    post = board.update(post_id, title, content)
    if not post:
        return render_template("404.html"), 404
    return redirect(url_for("show_post", post_id=post_id))

@app.route("/posts/<int:post_id>/delete", methods=["POST"])
def delete_post(post_id):
    ok = board.delete(post_id)
    if not ok:
        return render_template("404.html"), 404
    return redirect(url_for("list_posts"))

# API 예시
@app.route("/api/posts/<int:post_id>")
def api_post(post_id):
    post = board.get(post_id)
    if not post:
        return jsonify({"message":"없음"}), 404
    return jsonify(post)

if __name__ == "__main__":
    app.run(debug=True)
