#!/usr/bin/python3
"Flask web app that lists all the states with their cities"
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states():
    "List all states"
    states = storage.all(State).values()
    return render_template('9-states.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def state(id):
    "List all cities of a specific state"
    states = storage.all()
    state = states.get(f'State.{id}')
    return render_template('9-states.html', state=state)


@app.teardown_appcontext
def teardown(e):
    "Close the db connection"
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
