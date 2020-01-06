from time import sleep

from task_processors.completed_on_processor import CompletedOnProcessor
from task_processors.track_transition_processor import TrackTransitionProcessor


class PollingTaskProcessors():
    def __init__(self, notion_api):
        self.notion_api = notion_api

    def run(self):
        try:
            for row in self._build_task_query().execute():
                sleep(0.5)
                task = self.notion_api.client().get_block(row.id)
                self.process_task(task)

        except Exception as e:
            print(e)

    def process_task(self, task):
        print("Processing '{}'".format(task.title))

        CompletedOnProcessor(self.notion_api, task).run()
        TrackTransitionProcessor(self.notion_api, task).run()

    def _build_task_query(self):
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
        return self.notion_api.tasks_database().build_query(filter=filter_params, filter_operator="or")
