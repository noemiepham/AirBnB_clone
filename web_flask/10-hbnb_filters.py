#!/usr/bin/python3
"""Write a script that starts a Flask web application:"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)


@app.teardown_appcontext
def handle_teardown():
    """handle teardown"""
    storage.close()


@app.route('/states')
def states():
    """return all database"""
    state = storage.all(State)
    return render_template('9-states.py', state=state)


@app.route('/states/<id>')
def state_id():
    """return all database in the db"""
    cities = storage.all(City)
    return render_template('8-cities_by_states.py', cities=cities)


if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run('0.0.0.0', 5000)
