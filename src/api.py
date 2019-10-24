#!/usr/bin/env -S PATH="${PATH}:/usr/local/bin" python3

import os

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


@app.route('/add_note', methods=['POST'])
def add_note():
    try:
        if request.headers['token'] != os.getenv('API_TOKEN'):
            raise Exception('Request token does not match known value')

        notion_api = NotionApi()

        notion_api.append_to_current_day_notes(request.json['title'])

        return 'Succeceed in adding note', 200
    except Exception:
        return 'Failed in adding note', 500


@app.route('/add_task', methods=['POST'])
def add_task():
    try:
        if request.headers['token'] != os.getenv('API_TOKEN'):
            raise Exception('Request token does not match known value')

        notion_api = NotionApi()

        collection = notion_api.tasks_database().collection
        row = collection.add_row()
        row.name = request.json['title']
        row.status = 'Next Up'
        row.tags = [notion_api.config.imported_tag_url()]

        return 'Succeceed in adding task', 200
    except Exception:
        return 'Failed in adding task', 500


app.config.from_object(JobConfig())

scheduler = APScheduler()
scheduler.init_app(app)
scheduler.start()
