from notionscripts.notion_api import NotionApi
from notionscripts.already_deleted_error import AlreadyDeletedError

from .notion_api_page_helper import get_test_page, create_collection_view

from notion.block import TextBlock

import pytest  # noqa, F401


def clean_id(id):
    return id.replace("-", "")


def test_block_content(notion_token):
    notion_api = NotionApi(token=notion_token)
    test_page = get_test_page()

    block = test_page.children.add_new(TextBlock, title="test get block content")
    content = notion_api.block_content(block.id)

    assert content == {"id": clean_id(block.id), "block_type": "text", "title": "test get block content"}


def test_block_children(notion_token):
    notion_api = NotionApi(token=notion_token)
    test_page = get_test_page()

    block = test_page.children.add_new(TextBlock, title="a parent block")
    child_block_1 = block.children.add_new(TextBlock, title="child block 1")
    child_block_2 = block.children.add_new(TextBlock, title="child block 2")

    content = notion_api.block_children(block.id)

    assert content["parent"] == {"id": clean_id(block.id), "block_type": "text", "title": "a parent block"}
    assert content["children"][0] == {"id": clean_id(child_block_1.id), "block_type": "text", "title": "child block 1"}
    assert content["children"][1] == {"id": clean_id(child_block_2.id), "block_type": "text", "title": "child block 2"}


def test_block_append(notion_token):
    notion_api = NotionApi(token=notion_token)
    test_page = get_test_page()

    block = test_page.children.add_new(TextBlock, title="test block append")
    new_block = notion_api.block_append(block.id, {"title": "appending text"})

    assert new_block == {"id": clean_id(new_block.block.id), "block_type": "text", "title": "appending text"}
    assert clean_id(new_block.block.parent.id) == clean_id(block.id)


def test_block_update_with_text_block(notion_token):
    notion_api = NotionApi(token=notion_token)
    test_page = get_test_page()

    block = test_page.children.add_new(TextBlock, title="test block update")
    updated_block = notion_api.block_update(block.id, {"title": "test block has been updated"})

    assert updated_block == {"id": clean_id(block.id), "block_type": "text", "title": "test block has been updated"}


def test_block_update_with_collection_block(notion_token):
    notion_api = NotionApi(token=notion_token)

    collection_view = create_collection_view()
    block = collection_view.collection.add_row(name="test row", value=10, enabled=True)

    updated_block = notion_api.block_update(block.id, {"name": "test block has been updated", "value": 5})

    assert updated_block == {"id": clean_id(block.id), "block_type": "page", "name": "test block has been updated",
                             "value": 5, "category": None, "enabled": True, "tags": []}


def test_block_delete_with_text_block(notion_token):
    notion_api = NotionApi(token=notion_token)
    test_page = get_test_page()

    block = test_page.children.add_new(TextBlock, title="test block delete")
    parent_block = block.parent

    notion_api.block_delete(block.id)
    parent_block.refresh()

    assert block not in parent_block.children


def test_block_delete_with_collection_block(notion_token):
    notion_api = NotionApi(token=notion_token)

    collection_view = create_collection_view()
    block = collection_view.collection.add_row(name="test row", value=10, enabled=True)

    notion_api.block_delete(block.id)

    assert block not in collection_view.collection.get_rows()


def test_block_delete_an_already_deleted_block(notion_token):
    notion_api = NotionApi(token=notion_token)
    test_page = get_test_page()

    block = test_page.children.add_new(TextBlock, title="test block delete")
    parent_block = block.parent

    notion_api.block_delete(block.id)
    parent_block.refresh()

    with pytest.raises(AlreadyDeletedError):
        notion_api.block_delete(block.id)


def test_collection_view_content(notion_token):
    notion_api = NotionApi(token=notion_token)

    collection_view = create_collection_view()
    collection_id = collection_view.parent.id
    view_id = collection_view.id

    collection_view.collection.add_row(name="test row")
    collection_view_content = notion_api.collection_view_content(collection_id.replace("-", ""), view_id.replace("-", ""))

    assert collection_view_content["collection"] == {
        "collection_id": clean_id(collection_id),
        "view_id": clean_id(view_id),
        "collection_title": "Test collection",
        "view_title": "Test view"
    }
    assert collection_view_content["rows"][0]["name"] == "test row"


def test_collection_view_append(notion_token):
    notion_api = NotionApi(token=notion_token)

    collection_view = create_collection_view()
    collection_id = collection_view.parent.id.replace("-", "")
    view_id = collection_view.id.replace("-", "")

    notion_api.collection_append(collection_id, view_id, {"enabled": True, "value": 10, "name": "test row"})
    collection_view_content = notion_api.collection_view_content(collection_id, view_id)

    assert collection_view_content["rows"][0]["name"] == "test row"
    assert collection_view_content["rows"][0]["enabled"] is True
    assert collection_view_content["rows"][0]["value"] == 10
