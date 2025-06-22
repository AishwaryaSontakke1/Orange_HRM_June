import time

import pytest

from pageObjects.Login_Page import Login_Page_Class
from utilities.Logger import loggerClass
from utilities.readconfig import ReadConfig


@pytest.mark.usefixtures("driver_setup")
class Test_OrangeHRM_Login_001:
    driver = None
    login_url = ReadConfig.get_login_url()
    log = loggerClass.getLogger()



    def test_OrangeHRM_Login_params_004(self, get_data_for_login):
        self.log.info("test_OrangeHRM_Login_004 is started")
        username = get_data_for_login[0]
        password = get_data_for_login[1]
        expected_result = get_data_for_login[2]
        self.log.info("Opening url " + self.login_url)
        self.lp = Login_Page_Class(self.driver)
        self.log.info("Entering username")
        self.lp.enter_username(username)
        self.log.info("Entering password")
        self.lp.enter_password(password)
        self.log.info("Clicking login button")
        self.lp.click_login_button()
        self.log.info("Verifying login")
        if self.lp.verify_login() == "login pass":
            self.log.info("Login passed")
            self.log.info("Taking screenshot")
            self.driver.save_screenshot(".\\Screenshots\\test_OrangeHRM_Login_pass.png")
            self.log.info("Clicking menu button")
            self.lp.click_menu_button()
            self.log.info("Clicking logout button")
            self.lp.click_logout_button()
            Actual_result = "Login Pass"
        else:
            self.log.info("Login failed")
            self.log.info("Taking screenshot")
            self.driver.save_screenshot(".\\Screenshots\\test_OrangeHRM_Login_fail.png")
            Actual_result = "Login Fail"

        if Actual_result == expected_result:
            self.log.info("test_OrangeHRM_Login_004 is passed")
            assert True
        else:
            self.log.info("test_OrangeHRM_Login_004 is failed")
            assert False
        self.log.info("test_OrangeHRM_Login_004 is completed")




# pytest -v -s  -n auto --html=HTML_Reports/report.html --browser headless
# pytest -v -s  -n auto --html=HTML_Reports/chrome_report.html --browser chrome --alluredir=Allure_Reports
# allure serve Allure_Reports