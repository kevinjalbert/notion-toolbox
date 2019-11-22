#!/usr/local/bin/python3

import sys
import json

from notion_api import notion_api
from notion_api import config


try:
    database = notion_api.tags_database()
    results = database.default_query().execute()

    tags = [{
        "uid": row.id,
        "title": row.title,
        "variables": {"tagName": row.title},
        "arg": row.get_browseable_url(),
        "match": row.title,
        "copy": row.title,
        "largetype": row.title
    } for row in results]

    doneTag = [{
        "uid": "done",
        "title": "Done",
        "variables": {"tagName": "Done"},
        "arg": "Done",
        "match": "Done",
        "copy": "Done",
        "largetype": "Done"
    }]

    with open(config.tags_file_path(), "w") as outfile:
        json.dump({"items": doneTag + tags}, outfile)
    print(str(len(tags)) + " tags")
except Exception as e:
    # Print out nothing on STDOUT (missing value means means operation was unsuccessful)
    sys.stderr.write(e)
