#!/usr/local/bin/python3

import sys
import json

from notion_api import notion_api


try:

    lights = [{
        "uid": row["id"],
        "title": row["title"],
        "variables": {"lightName": row["title"]},
        "arg": row["url"],
        "match": row["title"],
        "copy": row["title"],
        "largetype": row["title"]
    } for row in notion_api.current_day_lights()]

    print(json.dumps({"items": lights}))
except Exception as e:
    # Print out nothing on STDOUT (missing value means means operation was unsuccessful)
    sys.stderr.write(e)
