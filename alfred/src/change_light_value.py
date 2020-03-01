#!/usr/local/bin/python3

import sys
import argparse
from datetime import datetime

from notion_api import notion_api


try:
    parser = argparse.ArgumentParser(
        description='Change value of selected light')
    parser.add_argument('--value', nargs='*', help='value (Yes/Half/No or empty)')
    parser.add_argument('--light', nargs='*', help='light id (notion url)')
    args = parser.parse_args(sys.argv[1].split())

    value = ' '.join(args.value)
    lightId = ' '.join(args.light)

    current_day = datetime.now().strftime("%A")

    block = notion_api.get_block(lightId)
    setattr(block, current_day, value)

    print(value)
except Exception as e:
    # Print out nothing on STDOUT (missing value means means operation was unsuccessful)
    sys.stderr.write(e)
