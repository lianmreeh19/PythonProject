import unittest
from KeremQA.page_object_example.pages.swaglabs_login_page import LoginPage
from KeremQA.page_object_example.tests.seleniumBaseExample import seleniumBaseExample

class sanityTest(unittest.TestCase):
    def setUp(self):
        self.base = seleniumBaseExample()
        self.driver = self.base.selenium_start_with_url("https://www.saucedemo.com/")
        self.login_page = LoginPage(self.driver)

    def tearDown(self):
        self.base.selenium_stop()

    def test_login_with_correct_parameters(self):
        print("into login with correct parameters")
        self.login_page.set_user_and_password("standard_user", "secret_sauce")
        self.login_page.click_on_login_button()
        assert self.driver.current_url == "https://www.saucedemo.com/inventory.html", "URL did not set as expected after logging in"

    def test_login_with_incorrect_password(self):
        print("into login with incorrect password")
        self.login_page.set_user_and_password("standard_user", "incorrect_password")
        self.login_page.click_on_login_button()
        assert self.driver.current_url == "https://www.saucedemo.com/", "URL did not set as expected after logging in"

    def test_login_with_incorrect_user(self):
        print("into login with incorrect user")
        self.login_page.set_user_and_password("incorrect_user", "secret_sauce")
        self.login_page.click_on_login_button()
        assert self.driver.current_url == "https://www.saucedemo.com/", "URL did not set as expected after logging in"

