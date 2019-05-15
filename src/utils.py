#!/usr/bin/env -S PATH="${PATH}:/usr/local/bin" python3


def app_url(browser_url):
    return browser_url.replace("https://www.notion.so/", "notion://")
