import time

import pytest
from selene import browser
from selenium import webdriver

@pytest.fixture(scope='function', autouse=True)
def browser_open():
    #browser.config.base_url = "https://demoqa.com/"
#    driver_options = webdriver.ChromeOptions()
#    driver_options.add_argument('--headless')
    browser.config.window_height = 3000
    browser.config.window_width = 1400
    browser.config.timeout = 4.0

    yield

    browser.quit()