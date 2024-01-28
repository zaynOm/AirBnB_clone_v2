#!/usr/bin/python3
"Flask web app that lists all the states with their cities"
from flask import Flask, render_template
from models import storage, storage_type
from models.state import State

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    "List all states with their cities"
    states = storage.all(State).values()
    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def teardown(e):
    "Close the db connection"
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
