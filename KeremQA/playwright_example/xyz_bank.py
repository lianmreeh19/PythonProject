from playwright.sync_api import sync_playwright, expect
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login")
    customer_login_button = page.get_by_role("button", name="Customer")
    customer_login_button.click()
    name_dropdown = page.locator("#userSelect")
    name_dropdown.select_option(index=2)
    login_button = page.get_by_role("button", name="Login")
    login_button.click()
    deposit_button = page.get_by_role("button", name="Deposit")
    deposit_button.click()
    url = page.url
    assert url == "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/account", "url is not correct"
    print("url is correct")