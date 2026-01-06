from playwright.sync_api import sync_playwright, expect
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://blazedemo.com/")
    departure_city = page.locator("[name='fromPort']")
    departure_city.select_option(index=2)
    destination_city = page.locator("[name='toPort']")
    destination_city.select_option(index=6)
    find_flights_button = page.get_by_role("button", name="Find")
    find_flights_button.click()
    home_button = page.locator("[href='home']")
    home_button.click()
    forgot_password_button = page.locator("[href='https://blazedemo.com/password/reset']")
    forgot_password_button.click()
    email_field = page.locator("[name='email']")
    email_field.type("user19@gmail.com")
    send_password_button = page.get_by_role("button", name="Send")
    send_password_button.click()
    url = page.url
    assert url == "https://blazedemo.com/password/email", "url is not correct"
    print("url is correct")