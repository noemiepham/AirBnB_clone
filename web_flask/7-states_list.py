#!/usr/bin/python3
"""Write a script that starts a Flask web application:"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def handle_teardown(self):
    """handle teardown"""
    storage.close()


@app.route('/states_list')
def hbnb7():
    """return all database in the db"""
    state = storage.all(State)
    return render_template('7-states_list.py', state=state)


if __name__ == '__main__':
     app.url_map.strict_slashes = False
     app.run('0.0.0.0', 5000)
