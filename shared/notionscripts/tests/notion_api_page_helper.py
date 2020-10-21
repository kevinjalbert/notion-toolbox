import pytest

from datetime import datetime
from notion.client import NotionClient
from notion.block import PageBlock, CollectionViewBlock

# Some parts of this file are inspired/using the code from notion-py
# https://github.com/jamalex/notion-py/blob/b7041ade477c1f59edab1b6fc025326d406dd92a/notion/smoke_test.py


def get_test_page():
    return test_page


@pytest.fixture(scope="session", autouse=True)
def setup_test_page(request, notion_token, notion_test_parent_page_id):
    global notion_client, test_page

    notion_client = NotionClient(token_v2=notion_token, monitor=False)
    test_page = create_test_page(notion_test_parent_page_id)

    yield

    test_page.remove(permanently=True)


def create_test_page(notion_test_parent_page_id):
    test_parent_page = notion_client.get_block(notion_test_parent_page_id)

    test_page = test_parent_page.children.add_new(
        PageBlock,
        title="Test page at {}".format(datetime.now().strftime("%Y-%m-%d %H:%M:%S")),
    )

    return test_page


def create_collection_view():
    schema = {
        "%9:q": {"name": "Enabled", "type": "checkbox"},
        "=d{|": {
            "name": "Tags",
            "type": "multi_select",
            "options": [
                {
                    "color": "orange",
                    "id": "79560dab-c776-43d1-9420-27f4011fcaec",
                    "value": "A",
                },
                {
                    "color": "default",
                    "id": "002c7016-ac57-413a-90a6-64afadfb0c44",
                    "value": "B",
                },
                {
                    "color": "blue",
                    "id": "77f431ab-aeb2-48c2-9e40-3a630fb86a5b",
                    "value": "C",
                },
            ],
        },
        "=d{q": {
            "name": "Category",
            "type": "select",
            "options": [
                {
                    "color": "orange",
                    "id": "59560dab-c776-43d1-9420-27f4011fcaec",
                    "value": "A",
                },
                {
                    "color": "default",
                    "id": "502c7016-ac57-413a-90a6-64afadfb0c44",
                    "value": "B",
                },
                {
                    "color": "blue",
                    "id": "57f431ab-aeb2-48c2-9e40-3a630fb86a5b",
                    "value": "C",
                },
            ],
        },
        "4Jv$": {"name": "Value", "type": "number"},
        "title": {"name": "Name", "type": "title"},
    }

    cvb = test_page.children.add_new(CollectionViewBlock)
    cvb.collection = notion_client.get_collection(
        notion_client.create_record("collection", parent=cvb, schema=schema)
    )
    cvb.title = "Test collection"
    view = cvb.views.add_new(view_type="table")

    return view
