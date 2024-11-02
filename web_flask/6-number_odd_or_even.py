#!/usr/bin/python3
"""Multiple pages"""

from flask import Flask, abort, render_template

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


@app.route("/number_template/<n>", strict_slashes=False)
def numbers_template(n):
    if n.isdigit():
        return render_template('5-number.html', n=n)
    else:
        abort(404)


@app.route("/number_odd_or_even/<n>", strict_slashes=False)
def numbers_odd_even(n):
    if n.isdigit():
        return render_template('6-number_odd_or_even.html', n=int(n))
    else:
        abort(404)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
