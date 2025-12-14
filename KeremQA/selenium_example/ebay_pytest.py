import time
import unittest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
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
        item = "Lian"
        input_items = self.driver.find_element(By.ID,"_nkw")
        input_items.send_keys(item)

    def test_keyboard_options_dropdown(self):
        advanced_button = self.driver.find_element(By.LINK_TEXT,"Advanced").click()
        keyboard_options = Select(self.driver.find_element(By.ID,"s0-1-20-4[0]-7[1]-_in_kw"))
        keyboard_options.select_by_index(3)
        item = "Lian"
        input_items = self.driver.find_element(By.ID,"_nkw")
        input_items.send_keys(item)
        input_items.send_keys(Keys.ENTER)
        time.sleep(3)
        url = self.driver.current_url
        assert item in url, "URL should contain the word 'Lian'"
        print("Item was found successfully")




