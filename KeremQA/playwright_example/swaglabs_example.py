from playwright.sync_api import sync_playwright, expect
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.saucedemo.com/")
    user_name = page.locator("#user-name")
    user_name.type("standard_user")
    password = page.locator("#password")
    password.type("secret_sauce")
    page.keyboard.press("Enter")
    url = page.url
    assert url == "https://www.saucedemo.com/inventory.html", "url is not correct"
    print(f"url: {url} is correct")
