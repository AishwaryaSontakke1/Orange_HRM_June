import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from utilities.readconfig import ReadConfig


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")

login_url = ReadConfig.get_login_url()

@pytest.fixture(scope="class")
def driver_setup(request):
    global driver
    browser = request.config.getoption("--browser")
    if browser == "chrome":
        print("Chrome browser is selected")
        driver = webdriver.Chrome()
    elif browser == "firefox":
        print("Firefox browser is selected")
        driver = webdriver.Firefox()
    elif browser == "edge":
        print("Edge browser is selected")
        driver = webdriver.Edge()
    elif browser == "headless":
        print("headless chrome browser selected")
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(options=chrome_options)
    else:
        print("Invalid browser name")

    #driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.get(login_url)
    driver.maximize_window()
    request.cls.driver = driver
    yield driver
    driver.quit()
    print("Browser is closed")





def pytest_metadata(metadata):
    # To add metadata
    metadata["Project Name"] = "ORANGE HRM"
    metadata["Environment"] = "Test"
    metadata["Tester Name"] = "Credence"
    metadata["URL"] = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login/"
    # To remove metadata
    del metadata["Platform"]




@pytest.fixture(params=[
    ("Admin", "admin123", "Login Pass"),
    ("Admin1", "admin123", "Login Fail"),
    ("Admin", "admin1231", "Login Fail"),
    ("Admin1", "admin1231", "Login Fail")
    ])
def get_data_for_login(request):
    return request.param

@pytest.fixture(params=[
    ("Naveen", "Kumar", "R", "Successfully Saved"),
    ("Anita", "R", "Sharma", "Successfully Saved"),
    ("Test", "", "User", "Successfully Saved")  # You can add a negative test too
])
def get_employee_data(request):
    return request.param
