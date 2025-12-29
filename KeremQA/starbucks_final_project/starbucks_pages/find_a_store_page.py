from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from KeremQA.starbucks_final_project.globals import NEW_YORK_STORE

class FindAStorePage():
    def __init__(self, driver):
        self.driver = driver

    def find_a_specific_store(self):
        print('Check specific store')
        new_york_store = self.driver.find_element(By.NAME, "place")
        new_york_store.send_keys(NEW_YORK_STORE)
        new_york_store.send_keys(Keys.ENTER)
        text = self.driver.find_element(By.CLASS_NAME, "flex.justify-between.content___DiNrm").text
        return text
