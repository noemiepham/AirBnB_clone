#!/usr/bin/python3
"""Write a script that starts a Flask web application:"""
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hbnb():
    """web application must be listening on 0.0.0.0, port 5000"""
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb1():
    """print HBNB"""
    return "HBNB"


if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run('0.0.0.0', 5000, debug=True)
