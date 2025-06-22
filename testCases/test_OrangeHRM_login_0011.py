import time

import pytest
from openpyxl.cell.text import InlineFont
from pytest_html.selfcontained_report import SelfContainedReport

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
           self.log.info("test_OrangeHRM_title_001 is passed")
           self.log.info("test_OrangeHRM_title_001 is passed")
           self.log.info("Taking screenshot")
           self.driver.save_screenshot(".\\Screenshot\\test_OrangeHRM_title_pass.png")
           assert True
        else:
            self.log.info("title is " + self.driver.title)
            self.log.info("test_OrangeHRM_title_001 is filed")
            self.log.info("Taking screenshot")
            self.driver.save_screenshot(".\\Screenshots\\test_OrangeHRM_title_fail.png")
            assert False
        self.log.info("test_OrangeHRM_title_001 is completed")












