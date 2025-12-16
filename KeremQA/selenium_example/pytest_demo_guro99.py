import unittest

from selenium.webdriver.common.by import By

from KeremQA.selenium_example.seleniumBaseKerem import seleniumBaseKerem

class demo_guro99_pytest(unittest.TestCase):
    def setUp(self):
        self.base = seleniumBaseKerem()
        self.driver = self.base.selenium_start_with_url("https://demo.guru99.com/test/newtours/reservation.php")

    def tearDown(self):
        self.base.selenium_stop()

    def test_one_way_checkbox(self):
        one_way_checkbox = self.driver.find_element(By.NAME, "tripType")
        one_way_checkbox.click()

        continue_button = self.driver.find_element(By.NAME, "findFlights")
        continue_button.click()
        url = self.driver.current_url
        assert "reservation2" in url, "URL should contain reservation2"
        print("test passed")