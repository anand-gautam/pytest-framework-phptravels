import pytest
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ConfigurationData.config_reader import read_config

@pytest.mark.usefixtures("setup")
class BaseClass:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, int(read_config("wait time", "WAIT_TIME")))

    def clear_text(self, by_locator):
        self.wait.until(EC.visibility_of_element_located(by_locator)).clear()

    def find_element(self, by_locator):
        return self.wait.until(EC.visibility_of_element_located(by_locator))

    def find_elements(self, by_locator):
        return self.wait.until(EC.visibility_of_all_elements_located(by_locator))

    def click_element(self, by_locator):
        self.wait.until(EC.element_to_be_clickable(by_locator)).click()

    def select_option_by_text(self, by_locator, text):
        element = self.wait.until(EC.visibility_of_element_located(by_locator))
        Select(element).select_by_visible_text(text)
        # sel.select_by_visible_text(text)

    def select_option_by_value(self, by_locator, value):
        element = self.wait.until(EC.visibility_of_element_located(by_locator))
        Select(element).select_by_value(value)

    def select_option_by_index(self, by_locator, index_num):
        element = self.wait.until(EC.visibility_of_element_located(by_locator))
        Select(element).select_by_value(index_num)

    def type_text(self, by_locator, value):
        self.wait.until(EC.visibility_of_element_located(by_locator)).send_keys(value)

    def wait_for(self, by_locator):
        self.wait.until(EC.visibility_of_element_located(by_locator))

    def get_element_text(self, by_locator):
        return self.wait.until(EC.visibility_of_element_located(by_locator)).text

