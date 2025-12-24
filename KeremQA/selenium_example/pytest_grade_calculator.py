import unittest

from selenium.webdriver.common.by import By

from KeremQA.selenium_example.seleniumBaseKerem import seleniumBaseKerem

class calculator(unittest.TestCase):
    def setUp(self):
        self.base = seleniumBaseKerem()
        self.driver = self.base.selenium_start_with_url("https://www.calculator.net/grade-calculator.html")

    def tearDown(self):
        self.base.selenium_stop()

    def test_grades_input(self):
        grade_1 = self.driver.find_element(By.NAME, "s1")
        grade_1.clear()
        grade_1.send_keys("97")
        grade_2 = self.driver.find_element(By.NAME, "s2")
        grade_2.clear()
        grade_2.send_keys("100")
        grade_3 = self.driver.find_element(By.NAME, "s3")
        grade_3.clear()
        grade_3.send_keys("88")

        calculate_button = self.driver.find_element(By.NAME, "x")
        calculate_button.click()

        grade_avg = self.driver.find_element(By.CSS_SELECTOR, "p[class='verybigtext']")
        text = grade_avg.text

        index_1 = text.index(":")+1
        index_2 = text.index("(")
        text = text[index_1:index_2].strip()
        text_as_float = float(text)
        is_pass = text_as_float >= 90
        assert is_pass, "the final grade is lower than 90"

        print(f"the average is: {text}")






