from flask import Flask, jsonify
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)

@app.route('/hello')
def hello():
    """
    A simple hello world endpoint.
    ---
    responses:
      200:
        description: A hello message
        schema:
          type: object
          properties:
            message:
              type: string
              example: Hello, World!
    """
    return jsonify(message="Hello, World!")

if __name__ == "__main__":
    app.run(debug=True)