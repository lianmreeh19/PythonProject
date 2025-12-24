import unittest
from selenium.webdriver.common.by import By
from KeremQA.selenium_example.seleniumBaseKerem import seleniumBaseKerem

class zara(unittest.TestCase):
    def setUp(self):
        self.base = seleniumBaseKerem()
        self.driver = self.base.selenium_start_with_url("https://www.zara.com/il/en/")

    def tearDown(self):
        self.base.selenium_stop()

    def test_shopping_bag(self):
        shopping_bag = self.driver.find_element(By.PARTIAL_LINK_TEXT, "SHOPPING")
        text = shopping_bag.text
        index_1 = text.index("[")
        index_2 = text.index("]")+1
        text = text[index_1:index_2]
        assert text == "[0]", "Shopping Bag text should be equal to [0]"
        print("test passed")

    def test_search_button(self):
        search_button = self.driver.find_element(By.LINK_TEXT, "SEARCH")
        search_button.click()

