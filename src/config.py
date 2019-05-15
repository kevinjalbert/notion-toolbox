#!/usr/bin/env -S PATH="${PATH}:/usr/local/bin" python3

import sys
import os
import json
from pathlib import Path


def tagsFilePath():
    return str(Path(__file__).parent.parent.absolute()) + "/data/tags.json"


def configFilePath():
    return str(Path(__file__).parent.parent.absolute()) + "/data/config.json"


def configJSON():
    try:
        if os.path.isfile(configFilePath()):
            with open(configFilePath()) as jsonFile:
                return json.load(jsonFile)
    except Exception as e:
        # Print out nothing on STDOUT (missing value means means operation was unsuccessful)
        sys.stderr.write(e)


def notionToken():
    return configJSON()['NOTION_TOKEN']


def tagsDatabaseURL():
    return configJSON()['TAGS_DATABASE_URL']


def tasksDatabaseURL():
    return configJSON()['TASKS_DATABASE_URL']


def winsDatabaseURL():
    return configJSON()['WINS_DATABASE_URL']


def yearPageURL():
    return configJSON()['YEAR_PAGE_URL']
