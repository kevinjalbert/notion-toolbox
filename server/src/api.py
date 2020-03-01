#!/usr/bin/env -S PATH="${PATH}:/usr/local/bin" python3

import os
from functools import wraps
from datetime import datetime

from notionscripts.notion_api import NotionApi
from utils import app_url
from polling_task_processors import PollingTaskProcessors

from flask import Flask, request, jsonify
from flask_apscheduler import APScheduler
app = Flask(__name__)


class JobConfig(object):
    JOBS = [
        {
            'id': 'polling_task_processors',
            'func': 'api:polling_task_processors',
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


def polling_task_processors():
    notion_api = NotionApi()
    PollingTaskProcessors(notion_api).run()


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


@app.route('/current_tasks.json', methods=['GET'])
@token_required
def get_current_tasks():
    try:
        notion_api = NotionApi()

        current_tasks = []
        for task in notion_api.get_current_tasks():
            current_tasks.append({'id': task.id, 'title': task.title})

        return jsonify(
            tasks=current_tasks
        )
    except Exception:
        return 'Failed fetching current tasks', 500


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


@app.route('/current_lights.json', methods=['GET'])
@token_required
def get_current_lights():
    try:
        notion_api = NotionApi()

        current_lights = []
        for light in notion_api.current_day_lights():
            current_lights.append({'id': light["url"], 'title': light["title"]})

        print(current_lights)
        return jsonify(
            lights=current_lights
        )
    except Exception:
        return 'Failed fetching current lights', 500


@app.route('/update_light.json', methods=['POST'])
@token_required
def update_light():
    try:
        notion_api = NotionApi()

        current_day = datetime.now().strftime("%A")

        block = notion_api.get_block(request.json['lightId'])
        setattr(block, current_day, request.json['value'])

        return 'Succeceed in updating light', 200
    except Exception:
        return 'Failed updating light', 500


app.config.from_object(JobConfig())

scheduler = APScheduler()
scheduler.init_app(app)
scheduler.start()
