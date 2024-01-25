#!/usr/bin/python3
"Is it a number?"
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


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    "display c"
    return f"C {text.replace('_', ' ')}"


@app.route("/python/", defaults={'text': 'is cool'}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text):
    "display python"
    return f"Python {text.replace('_', ' ')}"


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    "display n if it's a number"
    return f"{n} is a number"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
