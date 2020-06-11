#!/usr/bin/env -S PATH="${PATH}:/usr/local/bin" python3

from cachetools import cached
from datetime import datetime

from notion.client import NotionClient
from notion.block import DividerBlock, TextBlock, CollectionViewBlock

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

        week_number = current_date.isocalendar()[1]
        if self.config.week_starts_on_sunday():
            week_number = str(week_number + (current_date.isoweekday() == 7))

        for week_page in self.current_year().children:
            if week_page.title.startswith("Week {}".format(week_number)):
                found_week = week_page
                break
            else:
                continue

        return found_week

    @cached(cache={})
    def current_day(self):
        found_day = None
        current_date = datetime.now()

        day_name = current_date.strftime(self.config.custom_day_format())
        days_page = self.current_week().children[1].children[1]

        for day_page in days_page.children:
            if day_page.title.startswith(day_name):
                found_day = day_page
                break
            else:
                continue

        return found_day

    def current_week_lights(self):
        found_lights = None

        for block in self.current_week().children:
            if type(block) == CollectionViewBlock and block.title.endswith("Lights"):
                found_lights = block
                break
            else:
                continue

        return found_lights

    def current_day_lights(self):
        view = self.current_week_lights()

        if view is None:
            return

        current_day = datetime.now().strftime("%A")

        lights = []
        for row in view.collection.get_rows():
            if not row.objective or row.objective.startswith("["):
                continue

            lights.append({
                "id": row.id,
                "title": "{} ({})".format(row.objective, getattr(row, current_day) or " "),
                "url": row.get_browseable_url()
            })

        return lights

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
