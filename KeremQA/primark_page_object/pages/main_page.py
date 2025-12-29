from selenium.webdriver.common.by import By

class MainPage():
    def __init__(self, driver):
        self.driver = driver

    def click_button_and_get_text(self, text):
        button = self.driver.find_element(By.PARTIAL_LINK_TEXT, text)
        button_text = button.text
        button.click()
        return button_text

    def click_on_cart_button(self):
        self.driver.find_element(By.ID, "shopping-bag-link").click()

    def click_on_home_button(self):
        self.driver.find_element(By.CLASS_NAME, "LinkedLogo-logoImage").click()



