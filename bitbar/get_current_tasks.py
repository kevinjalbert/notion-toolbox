#!/usr/local/bin/python3

from notionscripts.notion_api import NotionApi
api = NotionApi()


def app_url(browser_url):
    return browser_url.replace("https://", "notion://")


message = None
for row in api.get_current_tasks():
    message = "%s | href=%s" % (row.title, app_url(row.get_browseable_url()))
    print(message)

if message is None:
    message = "Working on Nothing | href=%s" % app_url(api.current_day().get_browseable_url())
    print(message)
