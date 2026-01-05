from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://demo.guru99.com/test/newtours/index.php")
    user  = page.locator("[name='userName']")
    password = page.locator("[name='password']")

    user.fill("tutorial")
    password.fill("tutorial")
    submit = page.get_by_role("button",name="Submit")
    submit.click()
    flights = page.get_by_role("link",name="Flights")
    flights.click()

    from_dropdown = page.locator("[name='fromPort']")
    location = from_dropdown.select_option("Paris")
    print(location)
    print ("test end")