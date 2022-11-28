#!/usr/bin/python3
"""Write a script that starts a Flask web application:"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hbnb():
    """web application must be listening on 0.0.0.0, port 5000"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb1():
    """print HBNB"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def hbnb2(text):
    """print c + text"""
    return "C {}".format(text.replace("_", " "))

@app.route('/python/<text>', defaults={"text": "is cool"}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def hbnb3(text):
    """print text is cool + text"""
    return "Python {:s}".format(text.replace("_", " "))


if __name__ == '__main__':
    app.run('0.0.0.0', 5000, debug=True)  # host="0.0.0.0"
