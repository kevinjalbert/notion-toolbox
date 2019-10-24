#!/usr/bin/env -S PATH="${PATH}:/usr/local/bin" python3

import os
from functools import wraps

from notionscripts.notion_api import NotionApi
from utils import app_url

from flask import Flask, request, jsonify
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


def token_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if request.headers.get('api_token') == os.getenv('API_TOKEN'):
            return f(*args, **kwargs)
        elif request.json.get('api_token') == os.getenv('API_TOKEN'):
            return f(*args, **kwargs)
        elif request.args.get('api_token') == os.getenv('API_TOKEN'):
            return f(*args, **kwargs)
        else:
            return 'Request api_token does not match known value', 401
    return decorated_function


@app.route('/add_note', methods=['POST'])
@token_required
def add_note():
    try:
        notion_api = NotionApi()

        notion_api.append_to_current_day_notes(request.json['title'])

        return 'Succeceed in adding note', 200
    except Exception:
        return 'Failed in adding note', 500


@app.route('/add_task', methods=['POST'])
@token_required
def add_task():
    try:
        notion_api = NotionApi()

        collection = notion_api.tasks_database().collection
        row = collection.add_row()
        row.name = request.json['title']
        row.status = 'Next Up'
        row.tags = [notion_api.config.imported_tag_url()]

        return 'Succeceed in adding task', 200
    except Exception:
        return 'Failed in adding task', 500


@app.route('/current_links.json', methods=['GET'])
@token_required
def get_links():
    try:
        notion_api = NotionApi()

        current_day = notion_api.current_day()
        current_week = notion_api.current_week()

        return jsonify(
            current_day=app_url(current_day.get_browseable_url()),
            current_week=app_url(current_week.get_browseable_url()),
        )
    except Exception:
        return 'Failed fetching current links', 500


app.config.from_object(JobConfig())

scheduler = APScheduler()
scheduler.init_app(app)
scheduler.start()
