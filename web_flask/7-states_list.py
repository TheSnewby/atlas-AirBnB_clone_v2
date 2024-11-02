#!/usr/bin/python3
"""8. List of States"""
from flask import Flask, render_template, abort
from models import storage_type, storage
from models.state import State


app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    state_list = storage.all(State).sort()
    for state in state_list:
        state = "State: {}: <B>{}</B>".format(state.id, state.name)
    return render_template('7-states_list.html', state_list=state_list.)


@app.teardown_appcontext
def closer():
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
