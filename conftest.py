import time

import pytest
from selene import browser

@pytest.fixture(scope='function', autouse=True)
def browser_open():
    browser.config.window_height = 3000
    browser.config.window_width = 1400
    browser.config.timeout = 4.0

    yield

    time.sleep(2)
    browser.quit()