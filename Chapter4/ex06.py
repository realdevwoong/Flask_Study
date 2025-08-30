from flask import Flask, request, jsonify, Response
import json
app = Flask(__name__)
@app.route("/")
def home():
    return "Hello, Flask!"
# GET : 조회
@app.route("/list", methods=["GET"])
def get_items():
    return jsonify({"message": "모든 기록 조회"})

# POST : 생성
@app.route("/list", methods=["POST"])
def create_item():
    data = request.get_json()
    return jsonify({"message": "아이템 생성", "data": data}), 201
# curl -X POST http://127.0.0.1:5000/list \
#   -H "Content-Type: application/json" \
#   -d '{"title": "새 아이템", "content": "내용입니다"}'
#HTTP 메서드=POST
#전송하는 데이터 형식은 JSON이라고 서버에 알려줌
#데이터(data)를 요청 본문(body)에 넣어서 보내

# GET : 특정 아이템 조회
@app.route("/list/<int:list_id>", methods=["GET"])
def get_item(list_id):
    return jsonify({"message": f"{list_id}번 아이템 조회"})
# @app.route("/list/<int:list_id>")
# def get_item(list_id):
#     data = {"message": f"{list_id}번 아이템 조회"}
#     return Response(json.dumps(data, ensure_ascii=False), 
#                     content_type="application/json; charset=utf-8")
##파이썬 객체를 문자열 형태로 변환
##json.dumps() : 파이썬 객체를 JSON 문자열로 변환
##Response 객체를 사용하여 응답 생성
##ensure_ascii=False : 한글이 깨지지 않도록 설정 
# PUT : 수정
@app.route("/list/<int:list_id>", methods=["PUT"])
def update_item(list_id):
    data = request.get_json()
    return jsonify({"message": f"{list_id}번 아이템 수정", "data": data})
##curl -X PUT http://127.0.0.1:5000/list/1 \
##  -H "Content-Type: application/json" \
##  -d '{"title":"수정된 아이템","content":"수정된 내용"}'
# DELETE : 삭제
@app.route("/list/<int:list_id>", methods=["DELETE"])
def delete_item(list_id):
    return jsonify({"message": f"{list_id}번 아이템 삭제"})

if __name__ == "__main__":
    app.run(debug=True)

#curl -X POST http://127.0.0.1:5000/list \
#  -H "Content-Type: application/json" \
#  -d '{"title": "새 아이템", "content": "내용입니다"}'