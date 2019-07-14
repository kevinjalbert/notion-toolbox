#!/usr/bin/env -S PATH="${PATH}:/usr/local/bin" python3

import os
from cachetools import cached


@cached(cache={})
def notionToken():
    return os.environ.get('NOTION_TOKEN')


@cached(cache={})
def tasksDatabaseURL():
    return os.environ.get('TASKS_DATABASE_URL')


@cached(cache={})
def yearPageURL():
    return os.environ.get('YEAR_PAGE_URL')


@cached(cache={})
def importedTagURL():
    return os.environ.get('IMPORTED_TAG_URL')
