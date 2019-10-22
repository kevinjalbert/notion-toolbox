#!/usr/bin/env -S PATH="${PATH}:/usr/local/bin" python3

import sys
import json
import argparse

from notion_api import notion_api
from utils import app_url


try:
    collection = notion_api.tasks_database().collection

    parser = argparse.ArgumentParser(description='Add task')
    parser.add_argument('--status', nargs='*', help='status')
    parser.add_argument('--tags', nargs='*', help='tags (CSV-style)')
    parser.add_argument('--query', nargs=argparse.REMAINDER, help='query')
    args = parser.parse_args(sys.argv[1].split())

    query = ' '.join(args.query)
    status = ' '.join(args.status)

    row = collection.add_row()
    row.name = query
    row.status = status

    if args.tags:
        tags = ' '.join(args.tags).split(',')
        row.tags = tags

    # Print out alfred-formatted JSON (modifies variables while passing query through)
    output = {
        "alfredworkflow": {
            "arg": query,
            "variables": {
                "url": app_url(row.get_browseable_url())
            }
        }
    }
    print(json.dumps(output))
except Exception as e:
    # Print out nothing on STDOUT (missing value means means operation was unsuccessful)
    sys.stderr.write(e)
