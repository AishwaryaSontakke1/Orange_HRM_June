import time

import pytest
from faker import Faker

from pageObjects.Add_Employee_Page import Add_Employee_Page
from pageObjects.Login_Page import Login_Page_Class
from utilities.Logger import loggerClass
from utilities.readconfig import ReadConfig


@pytest.mark.usefixtures("driver_setup")
class Test_OrangeHRM_Add_Employee_004:
    driver = None
    login_url = ReadConfig.get_login_url()
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()
    log = loggerClass.getLogger()
    from pathlib import Path
    base_dir = Path(__file__).resolve().parent.parent
    image_path = Path(r"C:\Users\Admin\Pictures\Screenshots\Employee_photo.jpg")

    def test_OrangeHRM_Add_Employee_005(self):
        self.log.info("test_OrangeHRM_Add_Employee_004 is started")
        emp_id = Faker().random_int(min=100000, max=999999)
        self.ae = Add_Employee_Page(self.driver)
        self.log.info("Opening url " + self.login_url)
        self.log.info("Entering username")
        self.ae.enter_username(self.username)
        self.log.info("Entering password")
        self.ae.enter_password(self.password)
        self.log.info("Clicking login button")
        self.ae.click_login_button()
        self.log.info("Clicking PIM button")
        self.ae.Click_PIM()
        self.log.info("Clicking Add button")
        self.ae.Click_Add_Button()
        self.log.info("Entering first name")
        self.ae.Enter_First_Name("Naveen")
        self.log.info("Entering middle name")
        self.ae.Enter_Middle_Name("Kumar")
        self.log.info("Entering last name")
        self.ae.Enter_Last_Name("R")
        self.log.info("Clicking image upload button")
        self.ae.Click_Image_Upload(str(self.image_path))
        self.ae.Enter_Emp_ID(emp_id)
        self.log.info("Clicking save button")
        self.ae.Click_Save_Button()
        self.log.info("Verifying success message")
        print(self.ae.Get_Success_Message())
        if self.ae.Get_Success_Message() == "Successfully Saved":
            self.log.info("Employee added successfully")
            self.driver.save_screenshot(".\\Screenshots\\test_OrangeHRM_Add_Employee_005.png")
            assert True
        else:
            self.log.info("Employee not added successfully")
            self.driver.save_screenshot(".\\Screenshots\\test_OrangeHRM_Add_Employee_005.png")
            assert False

        self.log.info("test_OrangeHRM_Add_Employee_005 is completed")




# pytest -v -s  -n auto --html=HTML_Reports/report.html --browser headless
# pytest -v -s  -n auto --html=HTML_Reports/chrome_report.html --browser chrome --alluredir=Allure_Reports
# allure serve Allure_Reports


# Which argument required to pass below: (like headless--- > "headless")
# Warning: Potential Security Risk Ahead

# https://www.uitestingplayground.com/ -- > practice

# //div[@class='oxd-table-body']//div[1]//div[2]

# Orgin not origin

# dont use automation on any real site --> on most of the sites automation is not allowed or restricted.
# OTP or captcha --> These kind of things are commented in a test environment and
# no need to write anything for the automation tester or developers are using the fixed OTP and
# captcha for the functionality .

# 66% gm ford-->

# 1 lac
# 90k
