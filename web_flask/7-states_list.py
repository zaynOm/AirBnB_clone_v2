#!/usr/bin/python3
"Flask web app that lists all the states"
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    "List all the states"
    states = storage.all(State).values()
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown(e):
    "Close the db connection"
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
