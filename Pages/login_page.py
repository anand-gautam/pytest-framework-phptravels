from selenium.webdriver.common.by import By
from Pages.base_page import BaseClass


class LoginPage(BaseClass):

    user = (By.XPATH, "//input[@type='email']")
    password = (By.XPATH, "//input[@type='password']")
    btn_login = (By.XPATH, "//button[@type='submit']")
    dashboard_txt = (By.XPATH, "//*[@class='page-active']//*[text()=' Dashboard']")
    logout_btn = (By.XPATH, "//*[@class='sidebar-menu-wrap']//*[contains(text(), 'Logout')]")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def clear_user_email_txt(self):
        self.clear_text(LoginPage.user)

    def user_email(self, user_id):
        self.type_text(LoginPage.user, user_id)

    def clear_password(self):
        self.clear_text(LoginPage.password)

    def user_password(self, pw):
        self.type_text(LoginPage.password, pw)

    def click_login(self):
        self.click_element(LoginPage.btn_login)

    def logged_in(self):
        return self.get_element_text(LoginPage.dashboard_txt)


