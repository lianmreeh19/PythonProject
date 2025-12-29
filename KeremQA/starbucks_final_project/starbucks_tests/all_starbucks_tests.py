import unittest
from KeremQA.starbucks_final_project.globals import START_AN_ORDER_BUTTON, BASE_URL, EXPECTED_BUTTONS_LIST, \
    PROTEIN_CATEGORY
from KeremQA.starbucks_final_project.seleniumBaseStarbucks import seleniumBaseStarbucks, seleniumBaseStarbucks
from KeremQA.starbucks_final_project.starbucks_pages.find_a_store_page import FindAStorePage
from KeremQA.starbucks_final_project.starbucks_pages.giftcard_page import GiftCardPage
from KeremQA.starbucks_final_project.starbucks_pages.product_order_page import ProductOrderPage
from KeremQA.starbucks_final_project.starbucks_pages.welcome_page import WelcomePage

class starbucksTests(unittest.TestCase):
    def setUp(self):
        self.base = seleniumBaseStarbucks()
        self.driver = self.base.selenium_start_with_url(BASE_URL)
        self.welcome_page = WelcomePage(self.driver)
        self.product_order_page = ProductOrderPage(self.driver)
        self.giftcard_page = GiftCardPage(self.driver)
        self.find_a_store_page = FindAStorePage(self.driver)

    def tearDown(self):
        self.base.selenium_stop()

    def test_click_on_start_an_order_button(self):
        self.welcome_page.cookies_agree_button()
        print("into start an order test")
        self.welcome_page.click_on_start_an_order_button(START_AN_ORDER_BUTTON)
        url = self.driver.current_url
        assert url == "https://www.starbucks.com/menu", "The button Start An Order doesn't work as expected"
        print("The button Start An Order worked as expected")

    def test_end_to_end_drink_order(self):
        self.welcome_page.cookies_agree_button()
        self.welcome_page.click_on_start_an_order_button(START_AN_ORDER_BUTTON)
        print("into drink order test")
        text = self.product_order_page.choose_one_category_of_drinks(PROTEIN_CATEGORY)
        assert text == "High Protein Lattes", "This text: High Protein Lattes, should appear after picking Protein Beverages drinks category"
        print("picking Protein Beverages drinks category was made successfully")

        self.product_order_page.navigate_to_specific_drink_with_get()
        print("the drink Iced Vanilla Protein was chosen successfully")

        self.product_order_page.add_to_order_button()
        print("add to order button was clicked successfully")

        self.product_order_page.type_of_order()
        print("just browsing button was clicked successfully")

        text2 = self.product_order_page.check_if_sign_in_page_appears()
        assert text2 == "Sign in or create an account", "text2 should be: Sign in or create an account after clicking on add to order button"
        print("the sign in or create an account page appeared successfully after clicking on add to order button")

    def test_get_drink_text(self):
        self.welcome_page.cookies_agree_button()
        self.welcome_page.click_on_start_an_order_button(START_AN_ORDER_BUTTON)
        self.product_order_page.choose_one_category_of_drinks(PROTEIN_CATEGORY)
        text = self.product_order_page.choose_specific_drink()
        assert text == "Iced Vanilla Protein Latte", "text2 should be: Iced Vanilla Protein Latte, should appear"
        print("the drink Iced Vanilla Protein Latte is available")

    def test_click_on_home_page_button(self):
        self.welcome_page.cookies_agree_button()
        print("into click on home page button test")
        text = self.welcome_page.click_on_home_page_button()
        assert text == "Start an order", "text should be: Start an order, after clicking on home page button"
        print("click on home page button was made successfully")

    def test_available_giftcards(self):
        self.welcome_page.cookies_agree_button()
        self.welcome_page.click_on_giftcard_button()
        giftcards_amount = self.giftcard_page.get_giftcards_amount()
        assert giftcards_amount > 0, "there's no giftcards available"
        print("there is at least 1 available giftcard")

    def test_existing_buttons_at_welcome_page(self):
        self.welcome_page.cookies_agree_button()
        expected_buttons = EXPECTED_BUTTONS_LIST
        buttons = self.welcome_page.check_exist_buttons()
        assert expected_buttons == buttons, "the buttons: MENU, REWARDS, GIFT CARDS didn't found"
        print("the buttons: MENU, REWARDS and GIFT CARDS was found successfully at the welcome page")

    def test_find_specif_store(self):
        self.welcome_page.cookies_agree_button()
        self.welcome_page.click_on_find_a_store_button()
        store_text = self.find_a_store_page.find_a_specific_store()
        assert "New York" in store_text, "the result doesn't match search"
        print("the result matches the search")
























