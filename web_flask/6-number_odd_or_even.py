#!/usr/bin/python3
"""Write a script that starts a Flask web application:"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hbnb():
    """web application must be listening on 0.0.0.0, port 5000"""
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb1():
    """print HBNB"""
    return "HBNB"


@app.route('/c/<text>')
def hbnb2(text):
    """print c + text"""
    return "C {}".format(text.replace("_", " "))


@app.route('/python', defaults={"text": "is cool"})
@app.route('/python/<text>')
def hbnb3(text):
    """print text is cool + text"""
    return "Python {:s}".format(text.replace("_", " "))


@app.route('/number/<int:n>')
def hbnb4(n):
    """print n is integer"""
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>')
def hbnb5(n):
    """print n in h1"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>')
def number_odd_or_even(n):
    """print n in h1"""
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run('0.0.0.0', 5000, debug=True)
