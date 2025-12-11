import time
from time import sleep
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver
from KeremQA.selenium_example.seleniumBaseKerem import seleniumBaseKerem

base = seleniumBaseKerem()
driver = base.selenium_start_with_url("https://www.calculator.net/")
buttons = driver.find_elements(By.PARTIAL_LINK_TEXT, "Calculator")
for button in buttons:
    index = buttons.index(button)
    print(f"The button: {button.text}, found at index: {index}")

base.selenium_stop()