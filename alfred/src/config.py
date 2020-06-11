import sys
import os
import json
from pathlib import Path
from cachetools import cached


class Config():
    @cached(cache={})
    def tags_file_path(self):
        return str(Path(__file__).parent.parent.absolute()) + "/data/tags.json"

    @cached(cache={})
    def config_file_path(self):
        return str(Path(__file__).parent.parent.absolute()) + "/data/config.json"

    @cached(cache={})
    def config_json(self):
        try:
            if os.path.isfile(self.config_file_path()):
                with open(self.config_file_path()) as json_file:
                    return json.load(json_file)
        except Exception as e:
            # Print out nothing on STDOUT (missing value means means operation was unsuccessful)
            sys.stderr.write(e)

    @cached(cache={})
    def notion_token(self):
        return self.config_json()['NOTION_TOKEN']

    @cached(cache={})
    def tags_database_url(self):
        return self.config_json()['TAGS_DATABASE_URL']

    @cached(cache={})
    def tasks_database_url(self):
        return self.config_json()['TASKS_DATABASE_URL']

    @cached(cache={})
    def wins_database_url(self):
        return self.config_json()['WINS_DATABASE_URL']

    @cached(cache={})
    def year_page_url(self):
        return self.config_json()['YEAR_PAGE_URL']

    @cached(cache={})
    def week_starts_on_sunday(self):
        return self.config_json().get('WEEK_STARTS_ON_SUNDAY', True)

    @cached(cache={})
    def custom_day_format(self):
        return self.config_json().get('CUSTOM_DAY_FORMAT', "%B %-d")
