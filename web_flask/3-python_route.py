#!/usr/bin/python3
"""Write a script that starts a Flask web application:"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hbnb():
    """web application must be listening on 0.0.0.0, port 5000"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """print HBNB"""
    return "HBNB"


@app.route('/c/hbnb', strict_slashes=False)
def hbnb1():
    """print HBNB"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def hbnb2(text):
    """print c + text"""
    return "C {:s}".format(text.replace("_", " "))


@app.route('/python/<text>', strict_slashes=False)
def hbnb2(text):
    """print text is cool + text"""
    text = "is cool"
    return "C {:s}".format(text.replace("_", " "))


if __name__ == '__main__':
    app.run('0.0.0.0', 5000, debug=True)  # host="0.0.0.0"
