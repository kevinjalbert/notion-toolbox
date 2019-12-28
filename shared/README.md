Shared collection of common Notion scripts used in other tools in this repository.

## Usage

Some quick usage is shown here:

```python
from notionscripts.notion_api import NotionApi

notion_api = NotionApi()
notion_api.current_day()
notion_api.append_to_current_day_notes("title of a note")
```

For more detailed usage I would recommend taking a look at the [alfred](/../alfred/) and [server](/../server/) tools.

A more completed set of features and instructions will be provided soon.
