#!/usr/bin/env -S PATH="${PATH}:/usr/local/bin" python3

import os
from cachetools import cached


class Config():
    @cached(cache={})
    def notion_token(self):
        return os.environ.get('NOTION_TOKEN')

    @cached(cache={})
    def tasks_database_url(self):
        return os.environ.get('TASKS_DATABASE_URL')

    @cached(cache={})
    def tags_database_url(self):
        return os.environ.get('TAGS_DATABASE_URL')

    @cached(cache={})
    def wins_database_url(self):
        return os.environ.get('WINS_DATABASE_URL')

    @cached(cache={})
    def year_page_url(self):
        return os.environ.get('YEAR_PAGE_URL')

    @cached(cache={})
    def imported_tag_url(self):
        return os.environ.get('IMPORTED_TAG_URL')
