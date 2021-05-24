from app import app
from models.event_list import events
from models.event import Event
from flask import render_template
import datetime

@app.route('/')
def index():
    return "Hello!"

@app.route('/events')
def events_index():
    return render_template('index.html', title='Home', my_events=events)

#@app.route('/events')
# def add_new_event():

