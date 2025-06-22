from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Login_Page_Class:

    text_username_xpath = "//input[@placeholder='Username']"
    text_password_xpath = "//input[@placeholder='Password']"
    click_Login_button_xpath = "//button[@type='submit']"
    click_menu_button_xpath = "//p[@class='oxd-userdropdown-name']"
    click_logout_button_xpath = "//a[normalize-space()='Logout']"
    logo_OrangeHRM_xpath = "//img[@alt='company-branding']"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 5)


    def enter_username(self, username):
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.text_username_xpath)))
        self.driver.find_element(By.XPATH, self.text_username_xpath).clear()
        self.driver.find_element(By.XPATH, self.text_username_xpath).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.XPATH, self.text_password_xpath).clear()
        self.driver.find_element(By.XPATH, self.text_password_xpath).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(By.XPATH, self.click_Login_button_xpath).click()

    def click_menu_button(self):
        self.driver.find_element(By.XPATH, self.click_menu_button_xpath).click()

    def click_logout_button(self):
        self.driver.find_element(By.XPATH, self.click_logout_button_xpath).click()

    def verify_login(self):

        try :
            self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.click_menu_button_xpath)))
            return "login pass"
        except :
            return "login fail"

    def verify_Logo(self):
        try :
            self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.logo_OrangeHRM_xpath)))
            return "logo is present"
        except :
            return "logo is not present"