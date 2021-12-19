from Pages.base_page import BaseClass
from selenium.webdriver.common.by import By


class MainPage(BaseClass):

    sidebar_menu_items = (By.XPATH, "//*[contains(@class,'sidebar-menu')]//*[contains(@class,'list-items')]")
    main_menu_items = (By.CLASS_NAME, "main-menu-content")
    author_meta = (By.CLASS_NAME, "author__meta")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def sidebar_menu(self):
        return self.get_element_text(MainPage.sidebar_menu_items)

    def main_menu_content(self):
        return self.get_element_text(MainPage.main_menu_items)

    def welcome_text_left(self):
        return self.get_element_text(MainPage.author_meta)
    