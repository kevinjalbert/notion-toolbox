from notionscripts.notion_api import NotionApi

from .notion_api_page_helper import get_test_page, create_collection_view

from notion.block import TextBlock

import pytest


def test_block_content(notion_token):
    notion_api = NotionApi(token=notion_token)
    test_page = get_test_page()

    block = test_page.children.add_new(TextBlock, title="test get block content")
    content = notion_api.block_content(block.id)

    assert content == "test get block content"


@pytest.mark.focus
def test_block_append(notion_token):
    notion_api = NotionApi(token=notion_token)
    test_page = get_test_page()

    block = test_page.children.add_new(TextBlock, title="test block append")
    new_block = notion_api.block_append(block.id, "appending text")

    assert new_block.title == "appending text"
    assert new_block.parent.id == block.id


def test_collection_view_content(notion_token):
    notion_api = NotionApi(token=notion_token)

    collection_view = create_collection_view()
    collection_id = collection_view.parent.id.replace("-", "")
    view_id = collection_view.id.replace("-", "")

    collection_view.collection.add_row(name="test row")
    collection_view_content = notion_api.collection_view_content(collection_id, view_id)

    assert collection_view_content[0]["name"] == "test row"


def test_collection_view_append(notion_token):
    notion_api = NotionApi(token=notion_token)

    collection_view = create_collection_view()
    collection_id = collection_view.parent.id.replace("-", "")
    view_id = collection_view.id.replace("-", "")

    notion_api.collection_append(collection_id, view_id, {"enabled": True, "value": 10, "name": "test row"})
    collection_view_content = notion_api.collection_view_content(collection_id, view_id)

    assert collection_view_content[0]["name"] == "test row"
    assert collection_view_content[0]["enabled"] is True
    assert collection_view_content[0]["value"] == 10
