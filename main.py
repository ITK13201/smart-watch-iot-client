from flask import Flask, Response

from config.config import DEBUG


app = Flask(__name__)


@app.route("/")
def index() -> Response:
    return Response(response="<h1>No Content</h1>", status=204)


if __name__ == "__main__":
    app.run(port=8000, debug=DEBUG)
