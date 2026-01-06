from playwright.sync_api import sync_playwright, expect
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.calculator.net/")
    bmi_calculator = page.locator("[href='/bmi-calculator.html']")
    bmi_calculator.click()
    url = page.url
    assert url == "https://www.calculator.net/bmi-calculator.html", "url is not correct"
    print("url is correct")