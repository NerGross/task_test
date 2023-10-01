import pytest
from selenium import webdriver

import config
from sbis.pages.fixture import Fixture
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service


@pytest.fixture
def get_chrome_options():
    options = ChromeOptions()
    options.add_argument('chrome')
    options.add_argument('--start-maximized')
    # options.add_argument('--auto-open-devtools-for-tabs')
    options.add_argument('--ash-host-window-bounds=1920x1080')
    options.add_argument('--start-maximized')
    return options


@pytest.fixture
def get_webdriver(get_chrome_options):
    options = get_chrome_options
    PATH = Service(r"C:\chromedriver.exe")
    driver = webdriver.Chrome(service=PATH, options=options)
    return driver


@pytest.fixture(scope='function')
def setup(request, get_webdriver, sbis_fixture):
    driver = get_webdriver
    url = config.URL
    if request.cls is not None:
        request.cls.driver = driver
    driver.get(url)
    yield
    driver.delete_all_cookies()
    driver.quit()


# далее общие фикстуры
@pytest.fixture(scope='function')
def sbis_fixture():
    return Fixture
