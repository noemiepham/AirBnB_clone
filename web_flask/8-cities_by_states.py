#!/usr/bin/python3
"""Write a script that starts a Flask web application:"""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def handle_teardown():
    """handle teardown"""
    storage.close()


@app.route('/cities_by_states')
def hbnb9():
    """return all database in the db"""
    states = storage.all("States")
    return render_template('8-cities_by_states.html', states=states)


if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run('0.0.0.0', 5000)
