#!/usr/bin/env -S PATH="${PATH}:/usr/local/bin" python3

import sys
import os
import json
from pathlib import Path
from cachetools import cached


@cached(cache={})
def tagsFilePath():
    return str(Path(__file__).parent.parent.absolute()) + "/data/tags.json"


@cached(cache={})
def configFilePath():
    return str(Path(__file__).parent.parent.absolute()) + "/data/config.json"


@cached(cache={})
def configJSON():
    try:
        if os.path.isfile(configFilePath()):
            with open(configFilePath()) as jsonFile:
                return json.load(jsonFile)
    except Exception as e:
        # Print out nothing on STDOUT (missing value means means operation was unsuccessful)
        sys.stderr.write(e)


@cached(cache={})
def notionToken():
    return configJSON()['NOTION_TOKEN']


@cached(cache={})
def tagsDatabaseURL():
    return configJSON()['TAGS_DATABASE_URL']


@cached(cache={})
def tasksDatabaseURL():
    return configJSON()['TASKS_DATABASE_URL']


@cached(cache={})
def winsDatabaseURL():
    return configJSON()['WINS_DATABASE_URL']


@cached(cache={})
def yearPageURL():
    return configJSON()['YEAR_PAGE_URL']
