from selenium.webdriver.common.by import By

class ProductPage():
    def __init__(self, driver):
        self.driver = driver

    def click_on_girls_button(self):
        self.driver.find_element(By.LINK_TEXT, "GIRLS").click()


