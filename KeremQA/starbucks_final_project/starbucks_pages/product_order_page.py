from select import select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class ProductOrderPage():
    def __init__(self, driver):
        self.driver = driver

    def choose_one_category_of_drinks(self, text):
        print("testing choosing_one_category_of_drinks")
        drink_category = self.driver.find_element(By.PARTIAL_LINK_TEXT, text)
        drink_category.click()
        text = self.driver.find_element(By.CLASS_NAME, "sb-heading.text-md.pb3.text-bold").text
        return text

    def choose_specific_drink(self):
        print("testing choosing_specific_drink")
        text_drink = self.driver.find_element(By.CSS_SELECTOR, "a[href='/menu/product/28498/iced']").text
        return text_drink

    def navigate_to_specific_drink_with_get(self):
        print("navigate_to_specific_drink_with_get")
        self.driver.get("https://www.starbucks.com/menu/product/28498/iced")

    def choose_espresso_and_shots_options(self):
        print("testing espresso_and_shots_options")
        espresso_and_shots_options = self.driver.find_element(By.ID, "41-modifier-select")
        espresso_and_shots_options_as_dropdown = Select(espresso_and_shots_options)
        espresso_and_shots_options_as_dropdown.select_by_visible_text("Blonde Espresso")

    def click_on_customize_button(self):
        print("testing click_on_customize_button")
        customize_button = self.driver.find_element(By. CLASS_NAME, "sb-frap.sb-frap--centerSVG.sb-frap--houseGreen")
        customize_button.click()

    def add_to_order_button(self):
        print("testing add_to_order_button")
        add_to_order_button = self.driver.find_element(By.CSS_SELECTOR, "button[data-e2e='add-to-order-button']")
        add_to_order_button.click()

    def type_of_order(self):
        print("testing type_of_order")
        just_browsing_button = self.driver.find_element(By. CSS_SELECTOR, "button[type='button'")
        just_browsing_button.click()

    def check_if_sign_in_page_appears(self):
        print("check_if_sign_in_page_appears")
        sign_in_page = self.driver.find_element(By.CSS_SELECTOR, "div[class='sb-contentColumn__inner']").text
        return sign_in_page
        
