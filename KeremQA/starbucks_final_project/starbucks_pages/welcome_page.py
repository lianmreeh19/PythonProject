from selenium.webdriver.common.by import By

class WelcomePage():
    def __init__(self, driver):
        self.driver = driver

    def cookies_agree_button(self):
        cookies_agree_button = self.driver.find_element(By.ID, "truste-consent-button")
        cookies_agree_button.click()

    def click_on_start_an_order_button(self, text):
        print("testing click_on_start_an_order_button")
        start_an_order_button = self.driver.find_element(By.PARTIAL_LINK_TEXT, text)
        start_an_order_button.click()

    def click_on_home_page_button(self):
        print("testing click_on_home_page_button")
        rewards_button = self.driver.find_element(By.LINK_TEXT, "REWARDS")
        rewards_button.click()
        home_page_button = self.driver.find_element(By.CLASS_NAME, "block")
        home_page_button.click()
        start_an_order_button = self.driver.find_element(By. PARTIAL_LINK_TEXT, "Start").text
        return start_an_order_button

    def click_on_giftcard_button(self):
        print("testing click_on_giftcard_button")
        giftcard_button = self.driver.find_element(By. PARTIAL_LINK_TEXT, "GIFT")
        giftcard_button.click()