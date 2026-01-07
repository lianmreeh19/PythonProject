import time

from KeremQA.playwright_example.pages.login_page import loginPage

class TestLogin():
    def test_calculator_with_fixture_1(self, setup_playwright):
        page = setup_playwright
        page.goto("https://www.calculator.net/")
        print("test end")

    def test_calculator_with_fixture_2(self, setup_playwright_with_users):
        page = setup_playwright_with_users
        page.goto("https://www.calculator.net/")
        print("test end")

    def test_login_swaglabs_with_correct_parameters(self, setup_swaglabs):
        page, login_page, product_page, excel_utils = setup_swaglabs
        login_page.login("standard_user", "secret_sauce")
        login_page.verify_login_success()

    def test_login_swaglabs_with_incorrect_parameters(self, setup_swaglabs):
        page, login_page, product_page, excel_utils = setup_swaglabs
        login_page.login("standard_user", "fake")
        login_page.verify_login_fail()

    def test_get_prices_to_excel(self, setup_swaglabs):
        page, login_page, product_page, excel_utils = setup_swaglabs
        login_page.login("standard_user", "secret_sauce")
        prices = product_page.verify_and_get_prices()
        current_seconds = int(time.time())
        path = f"C:/Users/User/PycharmProjects/PythonProject/KeremQA/excel_files/prices_{current_seconds}.csv"
        excel_utils.set_excel_data(self, prices, path)
        excel_data = excel_utils.get_excel_column_data(self, 1, path)
        assert prices == excel_data, "data didn't read from excel as expected"
        print("data read from excel as expected")


