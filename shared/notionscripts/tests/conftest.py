import pytest

from .notion_api_page_helper import *  # noqa, F401


def pytest_addoption(parser):
    parser.addoption("--notion_token", action="store")
    parser.addoption("--notion_test_parent_page_id", action="store")


@pytest.fixture(scope="session")
def notion_token(request):
    value = request.config.option.notion_token
    if value is None:
        pytest.skip()
    return value


@pytest.fixture(scope="session")
def notion_test_parent_page_id(request):
    value = request.config.option.notion_test_parent_page_id
    if value is None:
        pytest.skip()
    return value
