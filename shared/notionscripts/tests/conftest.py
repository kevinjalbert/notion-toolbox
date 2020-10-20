import pytest


def pytest_addoption(parser):
    parser.addoption("--notion_token", action="store")


@pytest.fixture(scope='session')
def notion_token(request):
    value = request.config.option.notion_token
    if value is None:
        pytest.skip()
    return value
