import time

from selenium.webdriver import Keys
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.Login_Page import Login_Page_Class


class Add_Employee_Page(Login_Page_Class):
    click_pim_xpath = "//span[normalize-space()='PIM']"
    click_add_button_xpath = "//button[normalize-space()='Add']"
    text_first_name_xpath = "//input[@placeholder='First Name']"
    text_middle_name_xpath = "//input[@placeholder='Middle Name']"
    text_last_name_xpath = "//input[@placeholder='Last Name']"
    click_img_upload_xpath = "//input[@type='file']"
    click_save_button_xpath = "//button[normalize-space()='Save']"
    text_emp_id_xpath = "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/input[1]"
    success_message_xpath = "//p[@class='oxd-text oxd-text--p oxd-text--toast-message oxd-toast-content-text']"

    def Click_PIM(self):
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.click_pim_xpath)))
        self.driver.find_element(By.XPATH, self.click_pim_xpath).click()

    def Click_Add_Button(self):
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.click_add_button_xpath)))
        self.driver.find_element(By.XPATH, self.click_add_button_xpath).click()

    def Enter_First_Name(self, first_name):
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.text_first_name_xpath)))
        self.driver.find_element(By.XPATH, self.text_first_name_xpath).clear()
        self.driver.find_element(By.XPATH, self.text_first_name_xpath).send_keys(first_name)

    def Enter_Middle_Name(self, middle_name):
        self.driver.find_element(By.XPATH, self.text_middle_name_xpath).clear()
        self.driver.find_element(By.XPATH, self.text_middle_name_xpath).send_keys(middle_name)

    def Enter_Last_Name(self, last_name):
        self.driver.find_element(By.XPATH, self.text_last_name_xpath).clear()
        self.driver.find_element(By.XPATH, self.text_last_name_xpath).send_keys(last_name)

    def Click_Image_Upload(self, image_path):
        self.driver.find_element(By.XPATH, self.click_img_upload_xpath).send_keys(image_path)

    def Enter_Emp_ID(self, emp_id):
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.text_emp_id_xpath)))
        email_id = self.driver.find_element(By.XPATH, self.text_emp_id_xpath)
        email_id.send_keys(Keys.CONTROL + "a")
        email_id.send_keys(Keys.BACKSPACE)
        #time.sleep(10)
        email_id.send_keys(emp_id)

    def Click_Save_Button(self):
        self.driver.find_element(By.XPATH, self.click_save_button_xpath).click()

    def Get_Success_Message(self):
        try:
            WebDriverWait(self.driver, 10,0.2).until(expected_conditions.visibility_of_element_located((By.XPATH, self.success_message_xpath)))
            return self.driver.find_element(By.XPATH, self.success_message_xpath).text # Success
        except:
            return "Failed"
