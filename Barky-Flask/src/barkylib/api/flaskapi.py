"""
In looking at different refactors it appears this correlates wih the flask.api
Not sure if there is a difference between flask_sqlalchemy and sqlalchemy.
Also not completely understanding what the bus is vs a repository
"""

from datetime import datetime
from sqlalchemy import create_engine
from flask import Flask, jsonify, request
from barkylib.adapters.orm import start_mappers, metadata
from barkylib.domain import commands
from barkylib.api import views
from barkylib import bootstrap

app = Flask(__name__)
bus = bootstrap.bootstrap()

@app.route('/')
def index(self):
    return f'Barky API'

@app.route('/add_bookmark', methods=['POST'])
def add_bookmark():
    # title, url, notes, date_added, date_edited
    title = request.json["title"]
    url = request.json["url"]
    notes = request.json["notes"]
    date_added = request.json["date_added"]
    date_edited = request.json["date_edited"]

    cmd = commands.AddBookmarkCommand(
            title, url, notes, date_added, date_edited
    )
    bus.handle(cmd)
    return "OK", 201


@app.route("/bookmarks/<title>", methods=['GET'])
def get_bookmark_by_title(self, title):
    result = views.bookmarks_view(title, bus.uow)
    if not result:
         return "not found", 404
    return jsonify(result), 200

"""
tried to incorporate routes from other refactors
not sure why they were taken out or how thnigs are routed
"""
@app.route('/bookmarks/all')
def all(self):
    return f'all records' 

@app.route('/bookmarks/first/<property>/<value>/<sort>')
def many(self, filter, value, sort):
    pass   

def get_bookmark_by_id(self, title):
    pass

def delete(self, bookmark):
    pass

def update(self, bookmark):
    pass

if __name__ == "__main__":
    app.run()