from notionscripts.notion_api import NotionApi


def test_get_block_content(notion_token):
    notion_api = NotionApi(token=notion_token)
    block_id = "f91655c4122a44f49f19ea20db5dcdf7"

    content = notion_api.get_block_content(block_id)

    assert content == "Test block"


def test_get_collection_view(notion_token):
    notion_api = NotionApi(token=notion_token)
    collection_id = "4c2221595f184ccc8b8ffb490b4a4f90"
    view_id = "0f5afdd5859d45d9a3514c6e5cbe8cc6"
    collection_view = notion_api.get_collection_view(collection_id, view_id)

    assert collection_view.id == "0f5afdd5-859d-45d9-a351-4c6e5cbe8cc6"
