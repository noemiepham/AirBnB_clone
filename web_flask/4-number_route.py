#!/usr/bin/python3
''' script that starts a Flask web application '''

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    ''' Function that display Hello HBNB! '''
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    ''' Function that display HBNB '''
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def variable(text):
    ''' Function that display C + <text> '''
    return 'C ' + text.replace('_', ' ')


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text='is cool'):
    """Function that display python + text"""
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    ''' Function that display <n> '''
    return str(n) + ' is a number'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
