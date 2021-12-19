import pytest

from Pages.login_page import LoginPage
from Pages.main_page import MainPage
from Tests.base_test import BaseTest
from ConfigurationData.config_reader import read_config
from Utils.logger_utliity import GenerateLog

class TestLogin(BaseTest):

    logger = GenerateLog.create_log()
    sidebar_menu_assert = "Dashboard,  My Bookings,  Add Funds,  My Profile,  Logout"
    main_menu_assert = "Home, Hotels, Flights, Tours, Cars, Visa, Blog, Company"
    welcome_assert = "Welcome Back"

    @pytest.mark.smoke
    @pytest.mark.regression
    def test_login(self):
        self.logger.info("test_login: Test begins")
        self.driver.get(read_config("basic info", "url"))
        login_page = LoginPage(self.driver)
        self.logger.info("Entering user email")
        login_page.clear_user_email_txt()
        login_page.user_email(read_config("creds", "user_email"))
        self.logger.info("Entering user password")
        login_page.clear_password()
        login_page.user_password(read_config("creds", "user_pw"))
        self.logger.info("Clicking Login button and trying to login")
        login_page.click_login()
        self.logger.info("Asserting Login")
        login_assert = login_page.logged_in()
        assert login_assert.strip() == 'Dashboard', "Not logged in properly"
        self.logger.info("End of Test: test_login")

    @pytest.mark.regression
    def test_main_page(self):
        self.logger.info("main_page: Test beings")
        main_page = MainPage(self.driver)
        self.logger.info("Checking sidebar menu items")
        sidebar_text = main_page.sidebar_menu()
        sidebar_text_fmt = sidebar_text.replace("\n", ", ").strip()
        assert sidebar_text_fmt == self.sidebar_menu_assert, "Does not match"
        self.logger.info("Checking main menu items")
        main_mehu_text =  main_page.main_menu_content()
        main_menu_text_fmt = main_mehu_text.replace("\n", ", ").strip()
        assert main_menu_text_fmt == self.main_menu_assert, "Does not match"
        self.logger.info("Checking welcome time below profile icon")
        welcome_text = main_page.welcome_text_left().strip()
        assert welcome_text == self.welcome_assert, "Not in the right page"
        self.logger.info("End of Test: main_page")


