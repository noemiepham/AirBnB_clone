#!/usr/bin/python3
from flask import Flask
from gevent.pywsgi import WSGIServer
strict_slashes = False

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello HBNB"


if __name__ == '__main__':
    from waitress import serve

    app.run(host="0.0.0.0", port=5000, debug=True)  # host="0.0.0.0"
