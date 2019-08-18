from notionscripts.notion_api import NotionApi

from config import Config


notion_api = NotionApi(Config())
config = notion_api.config
