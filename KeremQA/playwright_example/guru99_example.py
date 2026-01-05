from playwright.sync_api import sync_playwright, expect
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://demo.guru99.com/test/newtours/")
    flights_button = page.get_by_role("link", name="Flights")
    flights_button.click()
    flights_url = page.url
    assert flights_url == "https://demo.guru99.com/test/newtours/reservation.php", "flights url is not correct"
    print("flights url is correct")

    hotels_button = page.get_by_role("link", name="Hotels")
    hotels_button.click()
    hotels_url = page.url
    assert hotels_url == "https://demo.guru99.com/test/newtours/support.php", "hotels url is not correct"
    print("hotels url is correct")