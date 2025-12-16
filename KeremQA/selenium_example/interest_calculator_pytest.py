import time
import unittest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from KeremQA.selenium_example.seleniumBaseKerem import seleniumBaseKerem

class interest_calculator(unittest.TestCase):
    def setUp(self):
        self.base = seleniumBaseKerem()
        self.driver = self.base.selenium_start_with_url("https://www.calculator.net/interest-calculator.html")

    def tearDown(self):
        self.base.selenium_stop()

    def test_set_parameters_field(self):
        initial_investment = self.driver.find_element(By.ID, "cstartingprinciple")
        initial_investment.clear()
        initial_investment.send_keys("3000")

        Annual_contribution = self.driver.find_element(By.ID, "cannualaddition")
        Annual_contribution.clear()
        Annual_contribution.send_keys("1000")

        end_radio_button = self.driver.find_elements(By.CLASS_NAME, "rbmark")
        self.base.click_on_element(end_radio_button[1])

        calculate_button = self.driver.find_element(By.NAME, "x")
        calculate_button.click()

        print_button = self.driver.find_element(By.LINK_TEXT, "Print")
        assert print_button.is_displayed(), "print button should be displayed"
        print("test pass")


