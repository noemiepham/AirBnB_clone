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
def hbnb10():
    """return state in db"""
    state = storage.all(State)
    return render_template('9-states.html', state=state)


@app.route('/states/<id>')
def hbnb11():
    """Displays an HTML page with info about <id>, if it exists"""
    for state in storage.all("States").values():
        if state.id == id:
            return render_template("9-states.html", state=state)
    return render_template("9-states.html")


if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run('0.0.0.0', 5000)
