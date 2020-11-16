from notionscripts.block_presenter import BlockPresenter

from .notion_api_page_helper import get_test_page, create_collection_view

from notion.block import TextBlock, DividerBlock

import json

import pytest  # noqa, F401


def clean_id(id):
    return id.replace("-", "")


def test_text_block_presentation(notion_token):
    test_page = get_test_page()

    block = test_page.children.add_new(TextBlock, title="textblock")
    assert BlockPresenter(block).block == block
    assert BlockPresenter(block) == {"id": clean_id(block.id), "block_type": "text", "title": "textblock"}
    assert json.dumps(BlockPresenter(block)) == '{"id": "%s", "block_type": "text", "title": "textblock"}' % clean_id(block.id)


def test_divider_block_presentation(notion_token):
    test_page = get_test_page()

    block = test_page.children.add_new(DividerBlock)
    assert BlockPresenter(block).block == block
    assert BlockPresenter(block) == {"id": clean_id(block.id), "block_type": "divider"}
    assert json.dumps(BlockPresenter(block)) == '{"id": "%s", "block_type": "divider"}' % clean_id(block.id)


def test_collection_row_block_presentation(notion_token):
    collection_view = create_collection_view()
    block = collection_view.collection.add_row(name="test row", value=10, enabled=True)

    assert BlockPresenter(block).block == block
    assert BlockPresenter(block) == {"id": clean_id(block.id), "block_type": "page", "enabled": True,
                                     "tags": [], "category": None, "value": 10, "name": "test row"}
    assert json.dumps(BlockPresenter(
        block)) == '{"id": "%s", "block_type": "page", "enabled": true, "tags": [], "category": null, "value": 10, "name": "test row"}' % clean_id(block.id)


def test_collection_view_presentation(notion_token):
    collection_view = create_collection_view()
    collection_view.name = "Test view"

    assert BlockPresenter(collection_view).block == collection_view
    assert BlockPresenter(collection_view) == {"collection_id": clean_id(collection_view.parent.id),
                                               "collection_title": "Test collection", "view_id": clean_id(collection_view.id), "view_title": "Test view"}

    json_string_template = '{"collection_id": "%s", "view_id": "%s", "collection_title": "Test collection", "view_title": "Test view"}'
    assert json.dumps(BlockPresenter(
        collection_view)) == json_string_template % (clean_id(collection_view.parent.id), clean_id(collection_view.id))
