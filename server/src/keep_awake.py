#!/usr/bin/env -S PATH="${PATH}:/usr/local/bin" python3

import requests


def ping():
    requests.get('https://notion-heroku.herokuapp.com/')
