import time

import pytest

from pageObjects.Login_Page import Login_Page_Class
from utilities.Logger import loggerClass
from utilities.readconfig import ReadConfig


@pytest.mark.usefixtures("driver_setup")
class Test_OrangeHRM_Login_001:
    driver = None
    login_url = ReadConfig.get_login_url()
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()
    log = loggerClass.getLogger()


    def test_OrangeHRM_title_001(self):
        self.log.info("test_OrangeHRM_title_001 is started")
        time.sleep(1)
        self.log.info("opening url " + self.login_url)
        self.log.info("Verifying title")
        if self.driver.title == "OrangeHRM":
            self.log.info("title is " + self.driver.title)
            self.log.info("test_OrangeHRM_title_001 is passed")
            self.log.info("Taking screenshot")
            self.driver.save_screenshot(".\\Screenshots\\test_OrangeHRM_title_pass.png")
            assert True
        else:
            self.log.info("title is " + self.driver.title)
            self.log.info("test_OrangeHRM_title_001 is failed")
            self.log.info("Taking screenshot")
            self.driver.save_screenshot(".\\Screenshots\\test_OrangeHRM_title_fail.png")
            assert False
        self.log.info("test_OrangeHRM_title_001 is completed")

    def test_OrangeHRM_Logo_002(self):
        self.log.info("test_OrangeHRM_Logo_002 is started")
        time.sleep(1)
        self.log.info("Verifying logo")
        self.lp = Login_Page_Class(self.driver)
        if self.lp.verify_Logo() == "logo is present":
            self.log.info("logo is present")
            self.log.info("test_OrangeHRM_Logo_002 is passed")
            self.log.info("Taking screenshot")
            self.driver.save_screenshot(".\\Screenshots\\test_OrangeHRM_Logo_pass.png")
            assert True
        else:
            self.log.info("logo is not present")
            self.log.info("test_OrangeHRM_Logo_002 is failed")
            self.log.info("Taking screenshot")
            self.driver.save_screenshot(".\\Screenshots\\test_OrangeHRM_Logo_fail.png")
            assert False
        self.log.info("test_OrangeHRM_Logo_002 is completed")

    def test_OrangeHRM_Login_003(self): # showing error in headless (-pdb)
        self.log.info("test_OrangeHRM_Login_003 is started")
        self.lp = Login_Page_Class(self.driver)
        self.log.info("Entering username")
        self.lp.enter_username(self.username)
        self.log.info("Entering password")
        self.lp.enter_password(self.password)
        self.log.info("Clicking login button")
        self.lp.click_login_button()
        self.log.info("Verifying login")
        if self.lp.verify_login() == "login pass":
            self.log.info("test_OrangeHRM_Login_003 is passed")
            self.log.info("Taking screenshot")
            self.driver.save_screenshot(".\\Screenshots\\test_OrangeHRM_Login_pass.png")
            self.log.info("Clicking menu button")
            self.lp.click_menu_button()
            self.log.info("Clicking logout button")
            self.lp.click_logout_button()
            assert True
        else:
            self.log.info("test_OrangeHRM_Login_003 is failed")
            self.log.info("Taking screenshot")
            self.driver.save_screenshot(".\\Screenshots\\test_OrangeHRM_Login_fail.png")
            assert False
        self.log.info("test_OrangeHRM_Login_003 is completed")




# pytest -v -s  -n auto --html=HTML_Reports/report.html --browser headless
# pytest -v -s  -n auto --html=HTML_Reports/chrome_report.html --browser chrome --alluredir=Allure_Reports
# allure serve Allure_Reports