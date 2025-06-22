# your task

import time
import pytest
from faker import Faker
from pathlib import Path

from pageObjects.Add_Employee_Page import Add_Employee_Page
from pageObjects.Login_Page import Login_Page_Class
from utilities.Logger import loggerClass
from utilities.readconfig import ReadConfig


@pytest.mark.usefixtures("driver_setup")
class Test_OrangeHRM_Add_Employee_Params_005:
    driver = None
    login_url = ReadConfig.get_login_url()
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()
    log = loggerClass.getLogger()
    image_path = r"C:\Users\Admin\Pictures\Screenshots\Employee_photo.jpg"

    def test_OrangeHRM_Add_Employee_params_006(self, get_employee_data):
        self.log.info("test_OrangeHRM_Add_Employee_params_005 started")
        emp_id = Faker().random_int(min=100000, max=999999)

        first_name, middle_name, last_name, expected_result = get_employee_data

        self.ae = Add_Employee_Page(self.driver)

        self.log.info("Opening URL: " + self.login_url)
        self.ae.enter_username(self.username)
        self.ae.enter_password(self.password)
        self.ae.click_login_button()

        self.log.info("Navigating to Add Employee page")
        self.ae.Click_PIM()
        self.ae.Click_Add_Button()

        self.ae.Enter_First_Name(first_name)
        self.ae.Enter_Middle_Name(middle_name)
        self.ae.Enter_Last_Name(last_name)
        self.ae.Click_Image_Upload(self.image_path)
        self.ae.Enter_Emp_ID(emp_id)
        self.ae.Click_Save_Button()

        actual_message = self.ae.Get_Success_Message()
        print(f"Success Message: {actual_message}")

        if actual_message == expected_result:
            self.log.info("Employee added successfully")
            self.driver.save_screenshot(f".\\Screenshots\\test_pass_{first_name}.png")
            assert True
        else:
            self.log.info("Employee addition failed")
            self.driver.save_screenshot(f".\\Screenshots\\test_fail_{first_name}.png")
            assert False

        self.log.info("test_OrangeHRM_Add_Employee_params_005 completed")



