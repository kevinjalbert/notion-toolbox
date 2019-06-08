#!/usr/bin/env -S PATH="${PATH}:/usr/local/bin" python3

import sys
import json

from notion_api import currentDayTasksDatabase
from utils import app_url

try:
    tasks = [{
        "uid": row.id,
        "title": "[" + row.status + "] " + row.title,
        "subtitle": "Tags: " + ", ".join([row.title for row in row.tags]),
        "variables": {"taskName": row.title, "url": app_url(row.get_browseable_url())},
        "arg": row.get_browseable_url(),
        "match": row.title + " " + row.status + " " + " ".join([row.title for row in row.tags]),
        "copy": row.title,
        "largetype": row.title
    } for row in currentDayTasksDatabase().views[0].default_query().execute()]

    print(json.dumps({"items": tasks}))
except Exception as e:
    # Print out nothing on STDOUT (missing value means means operation was unsuccessful)
    sys.stderr.write(e)
