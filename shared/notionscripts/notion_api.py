#!/usr/bin/env -S PATH="${PATH}:/usr/local/bin" python3

from cachetools import cached

from notion.client import NotionClient
from notion.block import TextBlock


class NotionApi():
    def __init__(self, token):
        self.token = token

    @cached(cache={})
    def client(self):
        return NotionClient(token_v2=self.token, monitor=False)

    def __collection_view(self, collection_id, view_id):
        return self.client().get_collection_view(f"https://www.notion.so/{collection_id}?v={view_id}")

    def block_content(self, block_id):
        block = self.client().get_block(block_id)

        content = [block.title]
        for child in block.children:
            if hasattr(child, "title"):
                content.append(child.title)

        return "\n".join(content)

    def block_append(self, block_id, text):
        block = self.client().get_block(block_id)

        return block.children.add_new(TextBlock, title=text)

    def collection_view_content(self, collection_id, view_id):
        collection_view = self.__collection_view(collection_id, view_id)
        results = collection_view.default_query().execute()

        content = []
        for row in results:
            content.append(row.get_all_properties())

        return content

    def collection_append(self, collection_id, view_id, data):
        collection_view = self.__collection_view(collection_id, view_id)

        row = collection_view.collection.add_row(**data)

        return row.get_all_properties()
