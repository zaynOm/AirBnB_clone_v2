#!/usr/bin/python3
"HBNB"
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    "say hello to flask"
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    "hbnb"
    return "HBNB"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
