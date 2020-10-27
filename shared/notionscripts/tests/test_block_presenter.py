from notionscripts.block_presenter import BlockPresenter

from .notion_api_page_helper import get_test_page, create_collection_view

from notion.block import TextBlock

import json

import pytest  # noqa, F401


def test_block_presentation(notion_token):
    test_page = get_test_page()

    block = test_page.children.add_new(TextBlock, title="textblock")

    assert BlockPresenter(block).block == block
    assert BlockPresenter(block) == {"id": block.id, "title": "textblock"}
    assert json.dumps(BlockPresenter(block)) == '{"id": "%s", "title": "textblock"}' % block.id


def test_collection_row_block_presentation(notion_token):
    collection_view = create_collection_view()
    block = collection_view.collection.add_row(name="test row", value=10, enabled=True)

    assert BlockPresenter(block).block == block
    assert BlockPresenter(block) == {"id": block.id, "enabled": True, "tags": [], "category": None, "value": 10, "name": "test row"}
    assert json.dumps(BlockPresenter(block)) == '{"id": "%s", "enabled": true, "tags": [], "category": null, "value": 10, "name": "test row"}' % block.id
