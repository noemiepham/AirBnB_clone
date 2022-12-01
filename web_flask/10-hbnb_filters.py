#!/usr/bin/python3
"""Write a script that starts a Flask web application:"""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def handle_teardown():
    """handle teardown"""
    storage.close()


@app.route('/hbnb_filters')
def hbnb_filters():
    """Displays the main HBnB filters HTML page"""
    states = storage.all("State")
    amenities = storage.all("Amenity")
    return render_template('10-hbnb_filters.html', states=states, amenities=amenities)


if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run('0.0.0.0', 5000)
