import unittest

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from KeremQA.selenium_example.seleniumBaseKerem import seleniumBaseKerem

class calculator(unittest.TestCase):
    def setUp(self):
        self.base = seleniumBaseKerem()
        self.driver = self.base.selenium_start_with_url("https://www.nike.com/il/")

    def tearDown(self):
        self.base.selenium_stop()

    def test_search_nike(self):
        search_field = self.driver.find_element(By.ID, "gn-search-input")
        search_field.clear()
        search_field.send_keys("shoes")
        search_field.send_keys(Keys.ENTER)

        elements = self.driver.find_elements(By.CLASS_NAME, "product-card__info.disable-animations")
        second_product_price = elements[1].text

        index_1 = second_product_price.index("₪") + 1
        price = second_product_price[index_1:]
        price = price.strip()
        price = float(price)


        assert (price < 1000), "price is higher than 1000"
        print(price)