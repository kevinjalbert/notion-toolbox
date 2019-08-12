#!/usr/bin/env -S PATH="${PATH}:/usr/local/bin" python3

from datetime import datetime
from time import sleep
from notion.block import ToggleBlock, TextBlock

from notion_api import client, tasksDatabase


def add_task_transitions():
    try:
        for row in _build_task_query().execute():
            sleep(0.5)

            task = client().get_block(row.id)

            print("Processing '{}'".format(task.title))

            # Find toggle block (or create one if it doesn't exist)
            toggle_block = _find_toggle_block(task)

            # Create initial transition if it doesn't exist
            if len(toggle_block.children) == 0:
                print("-> Initial Transition Detected")
                _create_transition(toggle_block, task)

            # Find last transition
            last_transition_block = toggle_block.children[-1]

            # Add next transition if task status is different
            if task.status not in last_transition_block.title:
                print("-> Transition Change Detected")
                _create_transition(toggle_block, task)

    except Exception as e:
        print(e)


def _build_task_query():
    filter_params = [
      {
        "property": "completed_on",
        "comparator": "date_is",
        "value_type": "today"
      },
      {
        "property": "completed_on",
        "comparator": "is_empty",
        "value_type": "exact_date"
      }
    ]
    return tasksDatabase().build_query(filter=filter_params, filter_operator="or")


def _find_toggle_block(task):
    toggle_block = None

    if len(task.children) == 0:
        toggle_block = task.children.add_new(ToggleBlock)

    if type(task.children[0]) == ToggleBlock:
        toggle_block = task.children[0]
    else:
        toggle_block = task.children.add_new(ToggleBlock)
        toggle_block.move_to(task.children[0], "before")

    toggle_block.title = "⏲️ Task Transitions ⏲️"

    return toggle_block


def _create_transition(toggle_block, task):
    transition_string = "{}, {}".format(task.status, _format_date_time(datetime.now()))
    toggle_block.children.add_new(TextBlock, title=transition_string)


def _format_date_time(datetime):
    return datetime.strftime("%Y-%m-%d %H:%M:%S")
