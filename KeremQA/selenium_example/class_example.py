import time
from time import sleep
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver
from KeremQA.selenium_example.seleniumBaseKerem import seleniumBaseKerem

base = seleniumBaseKerem()
driver = base.selenium_start_with_url("https://www.saucedemo.com/")
user=driver.find_element(By.ID,"user-name")
password =driver.find_element(By.NAME,"password")
login_button  = driver.find_element(By.ID,"login-button")

user.send_keys("standard_user")
password.send_keys("secret_sauce")
login_button.click()

first_price = driver.find_element(By.CLASS_NAME,"inventory_item_price")
price = first_price.text
print(price)
base.selenium_stop()