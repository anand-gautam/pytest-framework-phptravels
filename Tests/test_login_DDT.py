import pytest
from Pages.login_page import LoginPage
from Pages.main_page import MainPage
from Tests.base_test import BaseTest
from ConfigurationData.config_reader import read_config
from Utils.logger_utliity import GenerateLog
from Utils import excel_utility


@pytest.mark.ddt
@pytest.mark.smoke

@pytest.mark.regression
class TestLogin(BaseTest):
    logger = GenerateLog.create_log()
    xl_path = './DataFiles/data_provider.xlsx'

    def test_login(self):
        result_list = []
        self.logger.info("Test beings")
        self.driver.get(read_config("basic info", "url"))
        login_page = LoginPage(self.driver)
        self.rows = excel_utility.get_row_count(xl_path=TestLogin.xl_path, sheet_name='data')
        for row in range(2, self.rows + 1):
            self.user_email = excel_utility.read_cell_data(xl_path=TestLogin.xl_path, sheet_name='data', row_num=row,
                                                           col_num=1)
            self.user_pw = excel_utility.read_cell_data(xl_path=TestLogin.xl_path, sheet_name='data', row_num=row,
                                                        col_num=2)
            self.status = excel_utility.read_cell_data(xl_path=TestLogin.xl_path, sheet_name='data', row_num=row,
                                                       col_num=3)
            login_page.clear_user_email_txt()
            login_page.user_email(self.user_email)
            login_page.clear_password()
            login_page.user_password(self.user_pw)
            login_page.click_login()
            self.logger.info("Asserting Login")
            actual_title = self.driver.title
            expected_title = 'Dashboard - PHPTRAVELS'
            if actual_title == expected_title:
                if self.status == 'Pass':
                    self.logger.info("Passed")
                    excel_utility.write_data(xl_path=TestLogin.xl_path, sheet_name='data', row_num=row,
                                             col_num=4, data="Pass")
                    login_page.click_element(LoginPage.logout_btn)
                    login_page.wait_for(LoginPage.btn_login)
                    result_list.append("Pass")
                elif self.status == "Fail":
                    self.logger.info("Failed")
                    excel_utility.write_data(xl_path=TestLogin.xl_path, sheet_name='data', row_num=row,
                                             col_num=4, data="Fail")
                    login_page.wait_for(LoginPage.btn_login)
                    result_list.append("Fail")
            elif actual_title != expected_title:
                if self.status == "Pass":
                    self.logger.info("Failed")
                    excel_utility.write_data(xl_path=TestLogin.xl_path, sheet_name='data', row_num=row,
                                             col_num=4, data="Fail")
                    login_page.wait_for(LoginPage.btn_login)
                    result_list.append("Fail")
                elif self.status == 'Fail':
                    self.logger.info("Passed")
                    excel_utility.write_data(xl_path=TestLogin.xl_path, sheet_name='data', row_num=row,
                                             col_num=4, data="Fail")
                    login_page.wait_for(LoginPage.btn_login)
                    result_list.append("Passed")
        if "Fail" not in result_list:
            self.logger.info("DDT passed")
            assert True
        else:
            self.logger.info("DDT failed")
            assert False

        self.logger.info("End of Test")
