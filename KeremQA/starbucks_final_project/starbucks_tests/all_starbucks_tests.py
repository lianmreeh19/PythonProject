import time
import unittest
from KeremQA.starbucks_final_project.seleniumBaseStarbucks import seleniumBaseStarbucks, seleniumBaseStarbucks
from KeremQA.starbucks_final_project.starbucks_pages.giftcard_page import GiftCardPage
from KeremQA.starbucks_final_project.starbucks_pages.product_order_page import ProductOrderPage
from KeremQA.starbucks_final_project.starbucks_pages.welcome_page import WelcomePage

class starbucksTests(unittest.TestCase):
    def setUp(self):
        self.base = seleniumBaseStarbucks()
        self.driver = self.base.selenium_start_with_url("https://www.starbucks.com/")
        self.welcome_page = WelcomePage(self.driver)
        self.product_order_page = ProductOrderPage(self.driver)
        self.giftcard_page = GiftCardPage(self.driver)

    def tearDown(self):
        self.base.selenium_stop()

    def test_click_on_start_an_order_button(self):
        self.welcome_page.cookies_agree_button()
        print("into start an order test")
        self.welcome_page.click_on_start_an_order_button("Start an order")
        url = self.driver.current_url
        assert url == "https://www.starbucks.com/menu", "The button Start An Order doesn't work as expected"
        print("The button Start An Order worked as expected")

    def test_end_to_end_drink_order(self):
        self.welcome_page.cookies_agree_button()
        self.welcome_page.click_on_start_an_order_button("Start an order")
        print("into drink order test")
        text = self.product_order_page.choose_one_category_of_drinks("Protein")
        assert text == "High Protein Lattes", "This text: High Protein Lattes, should appear after picking Protein Beverages drinks category"
        print("picking Protein Beverages drinks category was made successfully")

        text2 = self.product_order_page.choose_specific_drink()
        assert text2 == "Iced Vanilla Protein Latte", "text2 should be: Iced Vanilla Protein Latte, should appear"
        print("the drink Iced Vanilla Protein Latte is available")

        self.product_order_page.navigate_to_specific_drink_with_get()
        print("the drink Iced Vanilla Protein was chosen successfully")

        self.product_order_page.add_to_order_button()
        print("add to order button was clicked successfully")

        self.product_order_page.type_of_order()
        print("just browsing button was clicked successfully")

        text3 = self.product_order_page.check_if_sign_in_page_appears()
        assert text3 == "Sign in or create an account", "text3 should be: Sign in or create an account after clicking on add to order button"
        print("the sign in or create an account page appeared successfully after clicking on add to order button")

    def test_click_on_home_page_button(self):
        self.welcome_page.cookies_agree_button()
        print("into click on home page button test")
        text = self.welcome_page.click_on_home_page_button()
        assert text == "Start an order", "text should be: Start an order, after clicking on home page button"
        print("click on home page button was made successfully")

    def test_that_one_giftcard_at_least_is_available(self):
        self.welcome_page.cookies_agree_button()
        self.welcome_page.click_on_giftcard_button()
        text = self.giftcard_page.check_if_giftcard_exists_and_click_on_it()
        assert text == "Gift Card", "text should be: Gift Card"





















