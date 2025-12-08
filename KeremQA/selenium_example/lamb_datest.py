import time
from time import sleep
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver
from KeremQA.selenium_example.seleniumBaseKerem import seleniumBaseKerem

base = seleniumBaseKerem()
driver = base.selenium_start_with_url("https://ecommerce-playground.lambdatest.io/")
elements = driver.find_elements(By.CLASS_NAME, "figure-img.img-fluid.lazy-load")
windows_button = elements[0]
windows_button.click()
prices = driver.find_elements(By.CLASS_NAME, "price-new")
for price in prices:
    all_prices = price.text
    print(all_prices)
base.selenium_stop()
