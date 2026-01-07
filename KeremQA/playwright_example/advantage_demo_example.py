from playwright.sync_api import sync_playwright, expect
with (sync_playwright() as p):
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://advantageonlineshopping.com/#/")
    contact_us = page.get_by_role("link", name="CONTACT")
    contact_us.click()
    email_field = page.locator("[name='emailContactUs']")
    email_field.type("user19@gmail.com")
    subject_field = page.locator("[name='subjectTextareaContactUs']")
    subject_field.type("buying product")
    send_button = page.locator("#send_btn")
    send_button.click()

    continue_shopping_button = page.get_by_text("CONTINUE SHOPPING")
    text = continue_shopping_button.inner_text()
    assert "CONTINUE SHOPPING" in text, "the button text not found"
    print("the button text was found successfully")
    continue_shopping_button.click()
    is_pass = not (continue_shopping_button.is_visible())
    assert is_pass, "continue button appears not as expected"
    print("continue shopping button didn't appear just as expected")
    
    browser.close()