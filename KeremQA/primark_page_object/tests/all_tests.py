import unittest
from KeremQA.primark_page_object.pages.cart_page import CartPage
from KeremQA.primark_page_object.pages.main_page import MainPage
from KeremQA.primark_page_object.pages.product_page import ProductPage
from KeremQA.primark_page_object.seleniumBasePrimark import seleniumBasePrimark

class AllTests(unittest.TestCase):
    def setUp(self):
        self.base = seleniumBasePrimark()
        self.driver = self.base.selenium_start_with_url("https://www.primark.com/en-gb")
        self.main_page = MainPage(self.driver)
        self.cart_page = CartPage(self.driver)
        self.product_page = ProductPage(self.driver)

    def tearDown(self):
        self.base.selenium_stop()

    def test_click_on_gift_card_button(self):
        button_text = self.main_page.click_button_and_get_text("Gift")
        assert button_text == "Gift Card", "gift card button text is not as expected"
        print("Gift card button text is as expected")

    def test_click_on_cart_button(self):
        self.main_page.click_on_cart_button()

    def test_get_cart_message(self):
        self.main_page.click_on_cart_button()
        self.cart_page.get_cart_message()

    def test_kids_url(self):
        button_text = self.main_page.click_button_and_get_text("KIDS")
        url = self.driver.current_url
        assert url == "https://www.primark.com/en-gb/c/kids", "kids url is not as expected"

    def test_click_on_home_button(self):
        self.main_page.click_button_and_get_text("KIDS")
        self.main_page.click_on_home_button()
        url = self.driver.current_url
        assert url == "https://www.primark.com/en-gb", "home button text is not as expected"
        print("home button text is as expected")

    def test_click_on_girls_button(self):
        self.main_page.click_button_and_get_text("KIDS")
        self.product_page.click_on_girls_button()
        url = self.driver.current_url
        assert url == "https://www.primark.com/en-gb/c/click-and-collect/l2/kids/girls", "girls button text is not as expected"
        print("Girs button text is as expected")



