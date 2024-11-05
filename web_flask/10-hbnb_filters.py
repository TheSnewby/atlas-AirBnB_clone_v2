#!/usr/bin/python3
"""9. Cities by States"""
from flask import Flask, render_template, abort
from models import storage
from models.state import State
from models.amenity import Amenity


app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def states_list():
    state_list = storage.all(State).values()
    state_list = sorted(state_list, key=lambda x: x.name)
    for state in state_list:
        if hasattr(state, 'cities'):
            state.cities = sorted(state.cities, key=lambda x: x.name)
        else:
            state.cities = sorted(state.cities(), key=lambda x: x.name)
    amen_list = storage.all(Amenity).values()
    amen_list = sorted(amen_list, key=lambda x: x.name)
    return render_template('8-cities_by_states.html',
                           state_list=state_list,
                           amenities_list=amen_list)


@app.teardown_appcontext
def closer(exception=None):
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
