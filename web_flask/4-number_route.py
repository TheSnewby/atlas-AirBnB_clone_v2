#!/usr/bin/python3
"""Multiple pages"""

from flask import Flask, abort

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def texts(text):
    return "C " + text.replace("_", " ")


@app.route("/python/", defaults={'text': 'is_cool'}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def pythons(text):
    return "Python " + text.replace("_", " ")


@app.route("/number/<n>", strict_slashes=False)
def numbers(n):
    if n.isdigit():
        return n + " is a number"
    else:
        abort(404)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
