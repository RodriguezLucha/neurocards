import pytest

from tests.drivers.ui import UIDriver


def pytest_addoption(parser):
    parser.addoption("--driver", action="store")


@pytest.fixture
def app_driver(request):
    selected = request.config.getoption("--driver")
    driver = None
    if selected == "ui":
        driver = UIDriver()
    else:
        raise Exception("Unknown driver. Available: ui")
    yield driver
