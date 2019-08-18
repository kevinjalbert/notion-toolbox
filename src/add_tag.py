#!/usr/bin/env -S PATH="${PATH}:/usr/local/bin" python3

import sys
import argparse

from notion_api import notion_api

try:
    collection = notion_api.tags_database().collection

    parser = argparse.ArgumentParser(description='Add tag')
    parser.add_argument('--query', nargs=argparse.REMAINDER, help='query')
    args = parser.parse_args(sys.argv[1].split())

    query = ' '.join(args.query)

    row = collection.add_row()
    row.name = query

    # Print out the added win (value printed means operation was successful)
    print(query)
except Exception as e:
    # Print out nothing on STDOUT (missing value means means operation was unsuccessful)
    sys.stderr.write(e)
