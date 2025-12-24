import time
import unittest
from selenium.webdriver.common.by import By
from KeremQA.selenium_example.seleniumBaseKerem import seleniumBaseKerem

class calculator(unittest.TestCase):
    def setUp(self):
        self.base = seleniumBaseKerem()
        self.driver = self.base.selenium_start_with_url("https://www.ebay.com/")

    def tearDown(self):
        self.base.selenium_stop()

    def test_search_and_price_text(self):
        search_field = self.driver.find_element(By.ID, "gh-ac")
        search_field.clear()
        search_field.send_keys("shoes")

        search_button = self.driver.find_element(By.ID, "gh-search-btn")
        search_button.click()

        time.sleep(3)
        price_text = self.driver.find_element(By.CLASS_NAME, "su-card-container__attributes.su-card-container__attributes--has-secondary")
        text = price_text.text
        if "shipping" in text:
            index_1 = text.index("+ILS")+4
            index_2 = text.index("shipping")
            shipping_price = text[index_1:index_2]
            shipping_price = shipping_price.strip()
            print(shipping_price)

        if "delivery" in text:
            index_1 = text.index("+ILS") + 4
            index_2 = text.index("delivery")
            shipping_price = text[index_1:index_2]
            shipping_price = shipping_price.strip()
            print(shipping_price)
