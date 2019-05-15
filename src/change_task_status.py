#!/usr/bin/env -S PATH="${PATH}:/usr/local/bin" python3

import sys
import argparse
from datetime import datetime

from notion_api import client

try:

    parser = argparse.ArgumentParser(
        description='Change status of selected task')
    parser.add_argument('--status', nargs='*', help='status')
    parser.add_argument('--task', nargs='*', help='task id (notion url)')
    args = parser.parse_args(sys.argv[1].split())

    status = ' '.join(args.status)
    taskId = ' '.join(args.task)

    record = client().get_block(taskId)
    record.status = status

    if status == "Completed":
        record.completed_on = datetime.now()

    print(status)
except Exception as e:
    # Print out nothing on STDOUT (missing value means means operation was unsuccessful)
    sys.stderr.write(e)
