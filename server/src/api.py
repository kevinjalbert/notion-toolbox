#!/usr/bin/env -S PATH="${PATH}:/usr/local/bin" python3

from functools import wraps

from notionscripts.notion_api import NotionApi

from flask import Flask, request, jsonify
from flask_apscheduler import APScheduler
app = Flask(__name__)


class JobConfig(object):
    JOBS = [
        {
            'id': 'ping',
            'func': 'keep_awake:ping',
            'args': (),
            'trigger': 'interval',
            'seconds': 600
        }
    ]

    SCHEDULER_API_ENABLED = True


def token_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'notion_token' in request.headers:
            return f(request.headers['Notion-Token'], *args, **kwargs)
        else:
            return 'Request is missing `Notion-Token` header (token_v2 from notion.so)', 401
    return decorated_function


@app.route('/blocks/<block_id>/append', methods=['POST'])
@token_required
def block_append(notion_token, block_id):
    try:
        notion_api = NotionApi(notion_token)

        block = notion_api.block_append(block_id, request.json['text'])

        return jsonify(block_id=block.id), 200
    except Exception as error:
        return jsonify(error=str(error)), 500


@app.route('/blocks/<block_id>/view', methods=['GET'])
@token_required
def block_view(notion_token, block_id):
    try:
        notion_api = NotionApi(notion_token)

        content = notion_api.block_content(block_id)

        return jsonify(content=content), 200
    except Exception as error:
        return jsonify(error=str(error)), 500


@app.route('/collections/<collection_id>/<view_id>/append', methods=['POST'])
@token_required
def collection_append(notion_token, collection_id, view_id):
    try:
        notion_api = NotionApi(notion_token)

        row = notion_api.collection_append(collection_id, view_id, request.json)

        return jsonify(row=row), 200
    except Exception as error:
        return jsonify(error=str(error)), 500


@app.route('/collections/<collection_id>/<view_id>/view', methods=['GET'])
@token_required
def collection_view(notion_token, collection_id, view_id):
    try:
        notion_api = NotionApi(notion_token)

        content = notion_api.collection_view(collection_id, view_id)

        return jsonify(rows=content), 200
    except Exception as error:
        return jsonify(error=str(error)), 500


app.config.from_object(JobConfig())

scheduler = APScheduler()
scheduler.init_app(app)
scheduler.start()
