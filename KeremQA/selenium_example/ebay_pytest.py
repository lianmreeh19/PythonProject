import unittest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from KeremQA.selenium_example.seleniumBaseKerem import seleniumBaseKerem

class ebay_pytest(unittest.TestCase):
    def setUp(self):
        self.base = seleniumBaseKerem()
        self.driver = self.base.selenium_start_with_url("https://www.ebay.com/")

    def tearDown(self):
        self.base.selenium_stop()

    def test_advanced_button(self):
        advanced_button = self.driver.find_element(By.LINK_TEXT,"Advanced").click()
        url = self.driver.current_url

        assert url == "https://www.ebay.com/sch/ebayadvsearch", "URL should be: https://www.ebay.com/sch/ebayadvsearch"
        print("Advanced button was clicked")

    def test_find_items(self):
        advanced_button = self.driver.find_element(By.LINK_TEXT,"Advanced").click()
        input_items = self.driver.find_element(By.ID,"_nkw")
        input_items.send_keys("Lian")
        input_items.send_keys(Keys.ENTER)
        url = self.driver.current_url
        assert "Lian" in url, "URL should contain the word 'Lian'"
        print(f"Item was found successfully")

