import time
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from KeremQA.selenium_example.seleniumBaseKerem import seleniumBaseKerem

class advDemoTest(unittest.TestCase):
    def setUp(self):
        self.base = seleniumBaseKerem()
        self.driver = self.base.selenium_start_with_url("https://advantageonlineshopping.com/#/")

    def tearDown(self):
        self.base.selenium_stop()

    def test_dropdown_example(self):
        time.sleep(5)
        contact_us = self.driver.find_element(By.PARTIAL_LINK_TEXT, "CONTACT")
        contact_us.click()
        category = self.driver.find_element(By.NAME, "categoryListboxContactUs")
        category_as_dropdown = Select(category)
        category_as_dropdown.select_by_index(2)
        category_as_dropdown.select_by_visible_text("Mice")

        product = self.driver.find_element(By.NAME, "productListboxContactUs")
        product_as_dropdown = Select(product)
        time.sleep(3)
        product_as_dropdown.select_by_index(2)

        email = self.driver.find_element(By.NAME, "emailContactUs")
        email.send_keys("demo@gmail.com")

        subject = self.driver.find_element(By.NAME, "subjectTextareaContactUs")
        subject.send_keys("buying a new mice")

        send_button = self.driver.find_element(By.ID, "send_btn")
        is_displayed = send_button.is_displayed()
        assert is_displayed == True, "Send button was not displayed"
        send_button.click()




