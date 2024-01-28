#!/usr/bin/python3
"Flask web app that lists all the states with their cities"
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity

app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def states():
    "List states, cities and amenities"
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    return render_template(
        "10-hbnb_filters.html", states=states, amenities=amenities
    )


@app.teardown_appcontext
def teardown(e):
    "Close the db connection"
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
