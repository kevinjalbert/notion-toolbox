#!/usr/local/bin/python3

import sys
import json

from notion_api import notion_api
from utils import app_url, fast_tags_for_task


try:
    tasks = [{
        "uid": row.id,
        "title": "[" + row.status + "] " + row.title,
        "subtitle": "Tags: " + fast_tags_for_task(row),
        "variables": {"taskName": row.title, "url": app_url(row.get_browseable_url())},
        "arg": row.get_browseable_url(),
        "match": row.title + " " + row.status + " " + fast_tags_for_task(row),
        "copy": row.title,
        "largetype": row.title
    } for row in notion_api.tasks_database().default_query().execute()]

    print(json.dumps({"items": tasks}))
except Exception as e:
    # Print out nothing on STDOUT (missing value means means operation was unsuccessful)
    sys.stderr.write(e)
