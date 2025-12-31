from selenium.webdriver.common.by import By
from KeremQA.starbucks_final_project.globals import GIFT_CARD_BUTTON
from KeremQA.starbucks_final_project.locators import WelcomePageLocators

class WelcomePage():
    def __init__(self, driver):
        self.driver = driver

    def cookies_agree_button(self):
        print("Cookies Agree")
        cookies_agree_button = self.driver.find_element(*WelcomePageLocators.COOKIES_AGREE_BUTTON_LOCATOR)
        cookies_agree_button.click()

    def click_on_start_an_order_button(self, text):
        print("testing click_on_start_an_order_button")
        start_an_order_button = self.driver.find_element(By.PARTIAL_LINK_TEXT, text)
        start_an_order_button.click()

    def click_on_home_page_button(self):
        print("testing click on home page button")
        rewards_button = self.driver.find_element(*WelcomePageLocators.REWARDS_BUTTON_LOCATOR)
        rewards_button.click()
        home_page_button = self.driver.find_element(*WelcomePageLocators.HOME_PAGE_BUTTON_LOCATOR)
        home_page_button.click()
        start_an_order_button = self.driver.find_element(*WelcomePageLocators.START_AN_ORDER_BUTTON_LOCATOR).text
        return start_an_order_button

    def click_on_gift_card_button(self):
        print("testing click on gift card button")
        gift_card_button = self.driver.find_element(By.PARTIAL_LINK_TEXT, GIFT_CARD_BUTTON)
        gift_card_button.click()

    def check_exist_buttons(self):
        print("checking exist buttons")
        buttons = self.driver.find_elements(*WelcomePageLocators.EXIST_BUTTONS_LOCATOR)
        buttons_list = []
        for button in buttons:
            button_text = button.text
            buttons_list.append(button_text)
        return buttons_list

    def click_on_find_a_store_button(self):
        print("testing click on find a store button")
        find_a_store_button = self.driver.find_element(*WelcomePageLocators.FIND_A_STORE_BUTTON_LOCATOR)
        find_a_store_button.click()
