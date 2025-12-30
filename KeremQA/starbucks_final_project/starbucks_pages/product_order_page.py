from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from KeremQA.starbucks_final_project.globals import ESPRESSO_TYPE
from KeremQA.starbucks_final_project.locators import ProductOrderPageLocators

class ProductOrderPage():
    def __init__(self, driver):
        self.driver = driver

    def choose_one_category_of_drinks(self, text):
        print("testing choose one category of drinks")
        drink_category = self.driver.find_element(By.PARTIAL_LINK_TEXT, text)
        drink_category.click()
        drink_category_text = self.driver.find_element(*ProductOrderPageLocators.DRINK_CATEGORY_TEXT_LOCATOR).text
        return drink_category_text

    def choose_specific_drink(self):
        print("testing choose specific drink")
        text_drink = self.driver.find_element(*ProductOrderPageLocators.TEXT_DRINK_LOCATOR).text
        return text_drink

    def navigate_to_specific_drink_with_get(self):
        print("navigating to specific drink with get url")
        self.driver.get("https://www.starbucks.com/menu/product/28498/iced")

    def choose_espresso_type(self):
        print("testing espresso and shots options")
        espresso_type = self.driver.find_element(*ProductOrderPageLocators.ESPRESSO_TYPE_LOCATOR)
        espresso_type_as_dropdown = Select(espresso_type)
        espresso_type_as_dropdown.select_by_visible_text(ESPRESSO_TYPE)

    def add_to_order_button(self):
        print("testing add to order button")
        add_to_order_button = self.driver.find_element(*ProductOrderPageLocators.ADD_TO_ORDER_BUTTON_LOCATOR)
        add_to_order_button.click()

    def type_of_order(self):
        print("testing type of order")
        just_browsing_button = self.driver.find_element(*ProductOrderPageLocators.JUST_BROWSING_BUTTON_LOCATOR)
        just_browsing_button.click()

    def check_if_sign_in_page_appears(self):
        print("checking if sign in page appears")
        sign_in_page = self.driver.find_element(*ProductOrderPageLocators.SIGN_IN_PAGE_LOCATOR).text
        return sign_in_page
        
