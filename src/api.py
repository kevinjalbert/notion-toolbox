#!/usr/bin/env -S PATH="${PATH}:/usr/local/bin" python3

from notion_api import appendToCurrentDayNotes, tasksDatabase
from config import importedTagURL

from flask import Flask, request
from flask_apscheduler import APScheduler
app = Flask(__name__)


class Config(object):
    JOBS = [
        {
            'id': 'add_task_transitions',
            'func': 'update_task_transitions:add_task_transitions',
            'args': (),
            'trigger': 'interval',
            'seconds': 60
        },
        {
            'id': 'ping',
            'func': 'keep_awake:ping',
            'args': (),
            'trigger': 'interval',
            'seconds': 600
        }
    ]

    SCHEDULER_API_ENABLED = True


@app.route('/add_note')
def add_note():
    try:
        note = request.args.get('title')

        appendToCurrentDayNotes(note)

        return 'Succeceed in adding note', 200
    except Exception:
        return 'Failed in adding note', 500


@app.route('/add_task')
def add_task():
    try:
        task = request.args.get('title')

        collection = tasksDatabase().collection
        row = collection.add_row()
        row.name = task
        row.status = 'Next Up'
        row.tags = [importedTagURL()]

        return 'Succeceed in adding task', 200
    except Exception:
        return 'Failed in adding task', 500


app.config.from_object(Config())

scheduler = APScheduler()
scheduler.init_app(app)
scheduler.start()
