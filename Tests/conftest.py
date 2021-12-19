import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chromeOptions
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import time


driver = None


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture(scope="session")
def get_browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="class")
def setup(request, get_browser):
    global driver
    if get_browser == "chrome":
        ch_options = chromeOptions()
        ch_options.add_argument("--start-maximized")
        ch_options.add_experimental_option('excludeSwitches', ['enable-logging'])
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=ch_options)
    elif get_browser == "firefox":
        firefox_options = Options()
        firefox_options.add_argument("--start-maximized")
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=firefox_options)
        driver.maximize_window()
    else:
        ch_options = chromeOptions()
        ch_options.add_argument("--start-maximized")
        ch_options.add_experimental_option('excludeSwitches', ['enable-logging'])
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=ch_options)

    request.cls.driver = driver
    yield
    time.sleep(2)
    driver.close()


def pytest_configure(config):
    config._metadata['Project Name'] = 'PHP Travels Customer Site'
    config._metadata['Tested By'] = 'Automated'

@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
