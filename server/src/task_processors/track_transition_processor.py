from datetime import datetime
from notion.block import ToggleBlock, TextBlock


class TrackTransitionProcessor():
    def __init__(self, notion_api, task):
        self.notion_api = notion_api
        self.task = task

    def run(self):
        try:
            # Find toggle block (or create one if it doesn't exist)
            toggle_block = self._find_toggle_block(self.task)

            # Create initial transition if it doesn't exist
            if len(toggle_block.children) == 0:
                print("-> Initial Transition Detected")
                self._create_transition(toggle_block, self.task)

            # Find last transition
            last_transition_block = toggle_block.children[-1]

            # Add next transition if task status is different
            if self.task.status not in last_transition_block.title:
                print("-> Transition Change Detected")
                self._create_transition(toggle_block, self.task)

        except Exception as e:
            print(e)

    def _find_toggle_block(self, task):
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

    def _create_transition(self, toggle_block, task):
        transition_string = "{}, {}".format(task.status, self._format_date_time(datetime.now()))
        toggle_block.children.add_new(TextBlock, title=transition_string)

    def _handle_recently_completed_task(self, task):
        if task.status == "Completed" and task.completed_on is None:
            print("-> Updating Task's 'Completed On'")
            task.completed_on = datetime.now()

    def _format_date_time(self, datetime):
        return datetime.strftime("%Y-%m-%d %H:%M:%S")
