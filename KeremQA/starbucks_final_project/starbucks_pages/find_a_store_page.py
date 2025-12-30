from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from KeremQA.starbucks_final_project.globals import NEW_YORK_STORE
from KeremQA.starbucks_final_project.locators import FindAStorePageLocators

class FindAStorePage():
    def __init__(self, driver):
        self.driver = driver

    def find_a_specific_store(self):
        print('Check specific store')
        new_york_store = self.driver.find_element(*FindAStorePageLocators.NEW_YORK_STORE_LOCATOR)
        new_york_store.send_keys(NEW_YORK_STORE)
        new_york_store.send_keys(Keys.ENTER)
        new_york_store_text = self.driver.find_element(*FindAStorePageLocators.NEW_YORK_STORE_TEXT_LOCATOR).text
        return new_york_store_text
