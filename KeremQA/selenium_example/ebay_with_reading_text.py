from selenium.webdriver.common.by import By
from KeremQA.selenium_example.seleniumBaseKerem import seleniumBaseKerem

base = seleniumBaseKerem()
driver = base.selenium_start_with_url("https://www.ebay.com/")
advanced_button= driver.find_element(By.LINK_TEXT, "Advanced")
advanced_text = advanced_button.text
if advanced_text == "Advanced":
    driver.find_element(By.LINK_TEXT, "Advanced").click()
    print(f"the URL for this page is {driver.current_url}")
else:
    print("it's not the right name of the button you test")

base.selenium_stop()