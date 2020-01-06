from datetime import datetime


class CompletedOnProcessor():
    def __init__(self, notion_api, task):
        self.notion_api = notion_api
        self.task = task

    def run(self):
        try:
            if self.task.status == "Completed" and self.task.completed_on is None:
                print("-> Updating Task's 'Completed On'")
                self.task.completed_on = datetime.now()

        except Exception as e:
            print(e)
