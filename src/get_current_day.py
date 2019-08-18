#!/usr/bin/env -S PATH="${PATH}:/usr/local/bin" python3

import sys

from notion_api import notion_api
from utils import app_url


try:
    print(app_url(notion_api.current_day().get_browseable_url()))
except Exception as e:
    # Print out nothing on STDOUT (missing value means means operation was unsuccessful)
    sys.stderr.write(e)
