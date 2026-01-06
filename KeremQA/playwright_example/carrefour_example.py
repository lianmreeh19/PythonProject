from playwright.sync_api import sync_playwright, expect
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.carrefour.com/en")
    cookies_button = page.locator("#onetrust-accept-btn-handler")
    cookies_button.click()
    activities_button_text = page.get_by_role("link", name="Stores")
    text = activities_button_text.text_content()
    assert text == "Stores", "the button Stores did not found"
    print("the button Stores was found")