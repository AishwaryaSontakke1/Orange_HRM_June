import time

import pytest

from pageObjects.Login_Page import Login_Page_Class
from utilities import Excel_Utilities
from utilities.Logger import loggerClass
from utilities.readconfig import ReadConfig


@pytest.mark.usefixtures("driver_setup")
class Test_OrangeHRM_Login_001:
    driver = None
    login_url = ReadConfig.get_login_url()
    log = loggerClass.getLogger()

    from pathlib import Path
    base_dir = Path(__file__).resolve().parent.parent
    excel_file_path = base_dir / "Test_Data" / "Test_Data.xlsx"
    #excel_path = ".\\TestData\\Test_Data.xlsx"
    sheet_name = "Sheet1"



    def test_OrangeHRM_Login_Excel_005(self):
        self.log.info("test_OrangeHRM_Login_005 is started")
        self.log.info("Opening url " + self.login_url)
        self.lp = Login_Page_Class(self.driver)
        self.log.info("Reading data from excel file")
        self.rows = Excel_Utilities.get_row_count(self.excel_file_path, self.sheet_name)
        result_list = []
        for r in range(2, self.rows + 1):
            username = Excel_Utilities.read_data(self.excel_file_path, self.sheet_name, r, 1)
            password = Excel_Utilities.read_data(self.excel_file_path, self.sheet_name, r, 2)
            expected_result = Excel_Utilities.read_data(self.excel_file_path, self.sheet_name, r, 3)

            self.log.info(f"Entering username-->{username}")
            self.lp.enter_username(username)
            self.log.info(f"Entering password-->{password}")
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
                Actual_result = "login pass"
            else:
                self.log.info("Login failed")
                self.log.info("Taking screenshot")
                self.driver.save_screenshot(".\\Screenshots\\test_OrangeHRM_Login_fail.png")
                Actual_result = "login fail"

            Excel_Utilities.write_data(self.excel_file_path, self.sheet_name, r, 4, Actual_result)

            if Actual_result == expected_result:

                testcase_status = "Pass"
            else:
                testcase_status = "Fail"

            result_list.append(testcase_status)

            Excel_Utilities.write_data(self.excel_file_path, self.sheet_name, r, 5, testcase_status)
            self.driver.get(self.login_url)
        print(result_list)
        if "Fail" not in result_list:
            self.log.info("test_OrangeHRM_Login_005 is passed")
            assert True
        else:
            self.log.info("test_OrangeHRM_Login_005 is failed")
            assert False


        self.log.info("test_OrangeHRM_Login_005 is completed")




# pytest -v -s  -n auto --html=HTML_Reports/report.html --browser headless
# pytest -v -s  -n auto --html=HTML_Reports/chrome_report.html --browser chrome --alluredir=Allure_Reports
# allure serve Allure_Reports

# D:\Batch Notes\Automation Testing may 2025\05. OrangeHRM_Pytest\Test_Data\Test_Data.xlsx