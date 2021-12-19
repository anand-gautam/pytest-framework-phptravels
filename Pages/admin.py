from selenium.webdriver.common.by import By

from ConfigurationData.config_reader import read_config
from Pages.base_page import BaseClass


class Admin(BaseClass):
    admin_email_id = (By.XPATH, "//input[@name='email']")
    admin_pw = (By.XPATH, "//input[@name='password']")
    btn_login = (By.XPATH, "//button[@type='submit']")
    logged_in_text = (By.XPATH, "//*[text()='DASHBOARD']")


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def admin_email(self):
        self.type_text(Admin.admin_email_id, read_config("creds", "admin_email"))

    def admin_password(self):
        self.type_text(Admin.admin_pw, read_config("creds", "admin_pw"))

    def admin_login_btn(self):
        self.click_element(Admin.btn_login)

    def wait_for_dashboard(self):
        self.wait_for(Admin.logged_in_text)

    def admin_logged_in(self):
        return  self.get_element_text(Admin.logged_in_text)



