from playwright.sync_api import sync_playwright, expect
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("http://www.ebay.com")
    assert page.title() == "Electronics, Cars, Fashion, Collectibles, Coupons and More | eBay"

    search = page.locator('#gh-ac')
    search.click()
    search.clear()
    search.fill("Phone")
    search_button = page.locator("#gh-search-btn")
    text_option_1 = search_button.inner_text()
    text_option_2 = search_button.text_content()
    search_button.click()
    print(page.url)
    print(text_option_1)
    print(text_option_2)

    browser.close()