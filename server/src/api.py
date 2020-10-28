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
        elif 'notion_token' in request.args:
            return f(request.args['notion_token'], *args, **kwargs)
        elif request.json is not None and 'notion_token' in request.json:
            # Popping the notion_token field as it would effect some of the
            # block updating as we use whole response for properties.
            notion_token = request.json.pop('notion_token')
            return f(notion_token, *args, **kwargs)
        else:
            return 'Request is missing `Notion-Token` header or `notion_token` in request body or `notion_token` in URL args.', 401
    return decorated_function


@app.route('/blocks/<block_id>/children', methods=['POST'])
@token_required
def block_children_append(notion_token, block_id):
    try:
        notion_api = NotionApi(notion_token)

        block = notion_api.block_append(block_id, request.json)

        return jsonify(block), 200
    except Exception as error:
        return jsonify(error=str(error)), 500


@app.route('/blocks/<block_id>', methods=['PUT'])
@token_required
def block_update(notion_token, block_id):
    try:
        notion_api = NotionApi(notion_token)

        block = notion_api.block_update(block_id, request.json)

        return jsonify(block), 200
    except Exception as error:
        return jsonify(error=str(error)), 500


@app.route('/blocks/<block_id>', methods=['DELETE'])
@token_required
def block_delete(notion_token, block_id):
    try:
        notion_api = NotionApi(notion_token)

        block = notion_api.block_delete(block_id)

        return jsonify(block), 200
    except Exception as error:
        return jsonify(error=str(error)), 500


@app.route('/blocks/<block_id>', methods=['GET'])
@token_required
def block_view(notion_token, block_id):
    try:
        notion_api = NotionApi(notion_token)

        block = notion_api.block_content(block_id)

        return jsonify(block), 200
    except Exception as error:
        return jsonify(error=str(error)), 500


@app.route('/blocks/<block_id>/children', methods=['GET'])
@token_required
def block_children_view(notion_token, block_id):
    try:
        notion_api = NotionApi(notion_token)

        children = notion_api.block_children(block_id)

        return jsonify(children=children), 200
    except Exception as error:
        return jsonify(error=str(error)), 500


@app.route('/collections/<collection_id>/<view_id>', methods=['POST'])
@token_required
def collection_append(notion_token, collection_id, view_id):
    try:
        notion_api = NotionApi(notion_token)

        row = notion_api.collection_append(collection_id, view_id, request.json)

        return jsonify(row), 200
    except Exception as error:
        return jsonify(error=str(error)), 500


@app.route('/collections/<collection_id>/<view_id>', methods=['GET'])
@token_required
def collection_view(notion_token, collection_id, view_id):
    try:
        notion_api = NotionApi(notion_token)

        content = notion_api.collection_view_content(collection_id, view_id)

        return jsonify(rows=content), 200
    except Exception as error:
        return jsonify(error=str(error)), 500


app.config.from_object(JobConfig())

scheduler = APScheduler()
scheduler.init_app(app)
scheduler.start()
