#!/usr/bin/python3
"""Write a script that starts a Flask web application:"""
from flask import Flask


app = Flask(__name__)


@app.route('/')
def hbnb():
    """web application must be listening on 0.0.0.0, port 5000"""
    return "Hello HBNB!"


if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
