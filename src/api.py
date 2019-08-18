#!/usr/bin/env -S PATH="${PATH}:/usr/local/bin" python3

from notionscripts.notion_api import NotionApi

from flask import Flask, request
from flask_apscheduler import APScheduler
app = Flask(__name__)


class JobConfig(object):
    JOBS = [
        {
            'id': 'add_task_transitions',
            'func': 'api:transition_tasks',
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


def transition_tasks():
    NotionApi().transition_tasks()


@app.route('/add_note')
def add_note():
    try:
        notion_api = NotionApi()

        note = request.args.get('title')

        notion_api.append_to_current_day_notes(note)

        return 'Succeceed in adding note', 200
    except Exception:
        return 'Failed in adding note', 500


@app.route('/add_task')
def add_task():
    try:
        notion_api = NotionApi()
        task = request.args.get('title')

        collection = notion_api.tasks_database().collection
        row = collection.add_row()
        row.name = task
        row.status = 'Next Up'
        row.tags = [notion_api.config.imported_tag_url()]

        return 'Succeceed in adding task', 200
    except Exception:
        return 'Failed in adding task', 500


app.config.from_object(JobConfig())

scheduler = APScheduler()
scheduler.init_app(app)
scheduler.start()
