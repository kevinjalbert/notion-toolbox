#!/usr/bin/env -S PATH="${PATH}:/usr/local/bin" python3

from cachetools import cached
from datetime import datetime

from notion.client import NotionClient
from notion.block import DividerBlock, TextBlock

from notionscripts.config import Config


class NotionApi():
    def __init__(self, config=Config()):
        self.config = config

    @cached(cache={})
    def client(self):
        return NotionClient(token_v2=self.config.notion_token(), monitor=False)

    @cached(cache={})
    def tags_database(self):
        return self.client().get_collection_view(self.config.tags_database_url())

    @cached(cache={})
    def tasks_database(self):
        return self.client().get_collection_view(self.config.tasks_database_url())

    @cached(cache={})
    def wins_database(self):
        return self.client().get_collection_view(self.config.wins_database_url())

    def get_block(self, id):
        return self.client().get_block(id)

    def append_text_to_block(self, block, text):
        return block.children.add_new(TextBlock, title=text)

    @cached(cache={})
    def current_year(self):
        return self.client().get_block(self.config.year_page_url())

    @cached(cache={})
    def current_week(self):
        found_week = None
        current_date = datetime.now()

        # Sunday Starts the week
        week_number = str(current_date.isocalendar()[
                         1] + (current_date.isoweekday() == 7))

        for week_page in self.current_year().children:
            if week_page.title.startswith("Week " + week_number):
                found_week = week_page
                break
            else:
                continue

        return found_week

    @cached(cache={})
    def current_day(self):
        found_day = None
        current_date = datetime.now()

        day_number = str(current_date.day)
        month_name = current_date.strftime("%B")
        days_page = self.current_week().children[1].children[1]

        for day_page in days_page.children:
            if day_page.title.startswith(month_name + " " + day_number):
                found_day = day_page
                break
            else:
                continue

        return found_day

    def append_to_current_day_notes(self, content):
        # Get the divider block that signifies the end of the notes for the current day
        divider_block = [x for x in self.current_day().children if type(x) == DividerBlock][0]

        # Add note to end of the page, then move it to before the divider
        note_block = self.current_day().children.add_new(TextBlock, title=content)
        note_block.move_to(divider_block, "before")

        return note_block

    def get_current_tasks(self):
        filter_params = {
            "filters": [
                {
                    "filter": {
                        "value": {
                            "type": "exact",
                            "value": "Current"
                        },
                        "operator": "enum_is"
                    },
                    "property": "status"
                },
            ]
        }
        current_tasks_query = self.tasks_database().build_query(filter=filter_params)
        return current_tasks_query.execute()
