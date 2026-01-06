from playwright.sync_api import sync_playwright, expect
with (sync_playwright() as p):
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://advantageonlineshopping.com/#/")
    contact_us = page.get_by_role("link", name="CONTACT")
    contact_us.click()
    # select_category = page.locator("[href='javascript:void(0)']")
    # select_category.select_option(index=1)
    # select_product = page.locator("[name='categoryListboxContactUs'")
    # select_product.select_option(index=4)
    email_field = page.locator("[name='emailContactUs']")
    page.keyboard.type("user19@gmail.com")
    subject_field = page.locator("[name='subjectTextareaContactUs']")
    page.keyboard.type("buying product")
    send_button = page.locator("[name='subjectTextareaContactUs']")
    assert send_button.is_enabled(), "filling details in contact us is failed"
    print("filling details in contact us is successful")