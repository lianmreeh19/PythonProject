from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from KeremQA.starbucks_final_project.globals import ESPRESSO_TYPE

class ProductOrderPage():
    def __init__(self, driver):
        self.driver = driver

    def choose_one_category_of_drinks(self, text):
        print("testing choose one category of drinks")
        drink_category = self.driver.find_element(By.PARTIAL_LINK_TEXT, text)
        drink_category.click()
        text = self.driver.find_element(By.CLASS_NAME, "sb-heading.text-md.pb3.text-bold").text
        return text

    def choose_specific_drink(self):
        print("testing choose specific drink")
        text_drink = self.driver.find_element(By.CSS_SELECTOR, "a[href='/menu/product/28498/iced']").text
        return text_drink

    def navigate_to_specific_drink_with_get(self):
        print("navigating to specific drink with get url")
        self.driver.get("https://www.starbucks.com/menu/product/28498/iced")

    def choose_espresso_type(self):
        print("testing espresso and shots options")
        espresso_type = self.driver.find_element(By.ID, "41-modifier-select")
        espresso_type_as_dropdown = Select(espresso_type)
        espresso_type_as_dropdown.select_by_visible_text(ESPRESSO_TYPE)

    def add_to_order_button(self):
        print("testing add to order button")
        add_to_order_button = self.driver.find_element(By.CSS_SELECTOR, "button[data-e2e='add-to-order-button']")
        add_to_order_button.click()

    def type_of_order(self):
        print("testing type of order")
        just_browsing_button = self.driver.find_element(By. CSS_SELECTOR, "button[type='button'")
        just_browsing_button.click()

    def check_if_sign_in_page_appears(self):
        print("checking if sign in page appears")
        sign_in_page = self.driver.find_element(By.CSS_SELECTOR, "div[class='sb-contentColumn__inner']").text
        return sign_in_page
        
