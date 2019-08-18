#!/usr/bin/env -S PATH="${PATH}:/usr/local/bin" python3

import sys
import argparse

from notion_api import notion_api


try:
    parser = argparse.ArgumentParser(description='Add note')
    parser.add_argument('--query', nargs=argparse.REMAINDER, help='query')
    args = parser.parse_args(sys.argv[1].split())

    query = ' '.join(args.query)

    print(notion_api.append_to_current_day_notes(query).title)
except Exception as e:
    # Print out nothing on STDOUT (missing value means means operation was unsuccessful)
    sys.stderr.write(e)
