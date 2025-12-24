import unittest
from selenium.common import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from KeremQA.selenium_example.seleniumBaseKerem import seleniumBaseKerem

class wolt(unittest.TestCase):
    def setUp(self):
        self.base = seleniumBaseKerem()
        self.driver = self.base.selenium_start_with_url("https://wolt.com/en/isr")

    def tearDown(self):
        self.base.selenium_stop()

    def test_search_location(self):
        try:
            search_field = self.driver.find_element(By.ID, "_R_tdj_")
            search_field.send_keys("Haifa")
            search_field.send_keys(Keys.ENTER)

        except NoSuchElementException:
            print("Element not found")

        finally:
            self.driver.get("https://wolt.com/en/discovery")





