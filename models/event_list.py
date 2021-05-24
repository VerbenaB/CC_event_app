from models.event import *
import datetime

event1 = Event(datetime.date(2021, 5, 20), "Y/A novels", 24, 5, "Discuss the phenomenom of Young Adult novels" )
event2 = Event(datetime.date(2021, 5, 22), "Poetry Masterclass", 15, 7, "The struggle of a poet")

events = [event1, event2]

# def add_event(event):
#     events.append(event)

