import time

import pytest
from selene import browser
from selenium import webdriver

@pytest.fixture(scope='function', autouse=True)
def browser_open():
    browser.config.base_url = "https://demoqa.com"
    driver_options = webdriver.ChromeOptions()
    driver_options.add_argument('--headless')
    browser.config.driver_options = driver_options
    browser.config.window_height = 1920
    browser.config.window_width = 1080
    browser.config.timeout = 4.0

    yield

    browser.quit()