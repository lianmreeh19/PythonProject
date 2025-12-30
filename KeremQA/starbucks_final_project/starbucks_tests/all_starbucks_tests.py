import unittest
from KeremQA.starbucks_final_project.globals import START_AN_ORDER_BUTTON, BASE_URL, EXPECTED_BUTTONS_LIST, \
    PROTEIN_CATEGORY
from KeremQA.starbucks_final_project.seleniumBaseStarbucks import seleniumBaseStarbucks, seleniumBaseStarbucks
from KeremQA.starbucks_final_project.starbucks_pages.find_a_store_page import FindAStorePage
from KeremQA.starbucks_final_project.starbucks_pages.gift_card_page import GiftCardPage
from KeremQA.starbucks_final_project.starbucks_pages.product_order_page import ProductOrderPage
from KeremQA.starbucks_final_project.starbucks_pages.welcome_page import WelcomePage


class starbucksTests(unittest.TestCase):
    def setUp(self):
        self.base = seleniumBaseStarbucks()
        self.driver = self.base.selenium_start_with_url(BASE_URL)
        self.welcome_page = WelcomePage(self.driver)
        self.product_order_page = ProductOrderPage(self.driver)
        self.gift_card_page = GiftCardPage(self.driver)
        self.find_a_store_page = FindAStorePage(self.driver)

    def tearDown(self):
        self.base.selenium_stop()

    def test_click_on_start_an_order_button(self):
        self.welcome_page.cookies_agree_button()
        print("into start an order test")
        self.welcome_page.click_on_start_an_order_button(START_AN_ORDER_BUTTON)
        url = self.driver.current_url
        assert url == "https://www.starbucks.com/menu", "The button 'Start An Order' doesn't work as expected"
        print("The button 'Start An Order' worked as expected")

    def test_end_to_end_drink_order(self):
        self.welcome_page.cookies_agree_button()
        self.welcome_page.click_on_start_an_order_button(START_AN_ORDER_BUTTON)
        print("into drink order test")
        category_text = self.product_order_page.choose_one_category_of_drinks(PROTEIN_CATEGORY)
        assert category_text == "High Protein Lattes", "The text 'High Protein Lattes' should appear after picking 'Protein Beverages' drinks category"
        print("Picking 'Protein Beverages' drinks category was made successfully")

        self.product_order_page.navigate_to_specific_drink_with_get()
        print("The drink 'Iced Vanilla Protein' was chosen successfully")

        self.product_order_page.add_to_order_button()
        print("'Add to order' button was clicked successfully")

        self.product_order_page.type_of_order()
        print("'Just browsing' button was clicked successfully")

        page_text = self.product_order_page.check_if_sign_in_page_appears()
        assert page_text == "Sign in or create an account", "page_text should be 'Sign in or create an account' after clicking on 'Add to order' button"
        print("The 'sign in or create an account' page appeared successfully after clicking on add to order button")

    def test_get_drink_text(self):
        print("into get drink text test")
        self.welcome_page.cookies_agree_button()
        self.welcome_page.click_on_start_an_order_button(START_AN_ORDER_BUTTON)
        self.product_order_page.choose_one_category_of_drinks(PROTEIN_CATEGORY)
        drink_text = self.product_order_page.choose_specific_drink()
        assert drink_text == "Iced Vanilla Protein Latte", "drink_text should be 'Iced Vanilla Protein Latte'"
        print("The drink Iced Vanilla Protein Latte is available")

    def test_click_on_home_page_button(self):
        print("into click on home page button test")
        self.welcome_page.cookies_agree_button()
        text = self.welcome_page.click_on_home_page_button()
        assert text == "Start an order", "text should be 'Start an order' after clicking on home page button"
        print("Click on home page button was made successfully")

    def test_available_gift_cards(self):
        print("into available gift cards test")
        self.welcome_page.cookies_agree_button()
        self.welcome_page.click_on_gift_card_button()
        gift_cards_amount = self.gift_card_page.get_gift_cards_amount()
        assert gift_cards_amount > 0, "There is no gift_cards available"
        print("There is at least 1 available gift card")

    def test_existing_buttons_at_welcome_page(self):
        print("into existing buttons at welcome page test")
        self.welcome_page.cookies_agree_button()
        expected_buttons = EXPECTED_BUTTONS_LIST
        buttons = self.welcome_page.check_exist_buttons()
        assert expected_buttons == buttons, "The buttons: MENU, REWARDS, GIFT CARDS didn't found at the welcome page"
        print("The buttons: MENU, REWARDS and GIFT CARDS was found successfully at the welcome page")

    def test_find_specific_store(self):
        print("into find specific store test")
        self.welcome_page.cookies_agree_button()
        self.welcome_page.click_on_find_a_store_button()
        store_text = self.find_a_store_page.find_a_specific_store()
        index1 = store_text.index("New")
        index2 = store_text.index("York") + 4
        new_store_text = store_text[index1:index2]
        assert new_store_text == "New York", "The result doesn't match search"
        print(f"The result is: {new_store_text}, and it matches the search")
