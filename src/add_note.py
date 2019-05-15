#!/usr/bin/env -S PATH="${PATH}:/usr/local/bin" python3

import sys
import argparse

from notion_api import appendToCurrentDayNotes

try:
    parser = argparse.ArgumentParser(description='Add note')
    parser.add_argument('--query', nargs=argparse.REMAINDER, help='query')
    args = parser.parse_args(sys.argv[1].split())

    query = ' '.join(args.query)

    print(appendToCurrentDayNotes(query).title)
except Exception as e:
    # Print out nothing on STDOUT (missing value means means operation was unsuccessful)
    sys.stderr.write(e)
