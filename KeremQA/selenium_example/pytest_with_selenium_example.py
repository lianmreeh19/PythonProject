import time
import unittest
from selenium.webdriver.common.by import By
from KeremQA.selenium_example.seleniumBaseKerem import seleniumBaseKerem

class pytest_swaglabs(unittest.TestCase):
    def setUp(self):
        self.base = seleniumBaseKerem()
        self.driver = self.base.selenium_start_with_url("https://www.saucedemo.com/")

    def tearDown(self):
        self.base.selenium_stop()

    def test_login_correct_details(self):
        print("into test login")
        user = self.driver.find_element(By.ID, "user-name")
        password = self.driver.find_element(By.NAME, "password")
        login_button = self.driver.find_element(By.ID, "login-button")

        user.send_keys("standard_user")
        password.send_keys("secret_sauce")
        login_button.click()
        url = self.driver.current_url
        assert url == "https://www.saucedemo.com/inventory.html", ("URL should be: https://www.saucedemo.com/inventory.html")

    def test_login_incorrect_details(self):
        user = self.driver.find_element(By.ID, "user-name")
        password = self.driver.find_element(By.NAME, "password")
        login_button = self.driver.find_element(By.ID, "login-button")

        user.send_keys("standard_userrrrr")
        password.send_keys("secret_sauce")
        login_button.click()
        time.sleep(2) # example of delay
        url = self.driver.current_url
        assert url == "https://www.saucedemo.com/", "URL should be: https://www.saucedemo.com/"
