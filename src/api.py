#!/usr/bin/env -S PATH="${PATH}:/usr/local/bin" python3

from notion_api import appendToCurrentDayNotes

from flask import Flask, request
app = Flask(__name__)


@app.route('/add_note')
def add_note():
    try:
        note = request.args.get('title')
        appendToCurrentDayNotes(note)
        return 'Succeceed in adding note', 200
    except Exception:
        return 'Failed in adding note', 500
