#!/usr/bin/env -S PATH="${PATH}:/usr/local/bin" python3

import sys

from utils import app_url
from notion_api import currentDay

try:
    print(app_url(currentDay().get_browseable_url()))
except Exception as e:
    # Print out nothing on STDOUT (missing value means means operation was unsuccessful)
    sys.stderr.write(e)
