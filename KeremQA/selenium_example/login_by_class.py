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
elements = driver.find_elements(By.CLASS_NAME,"input_error.form_input")
user = elements[0]
user.send_keys("standard_user")
password = elements[1]
password.send_keys("secret_sauce")
login_button = driver.find_element(By.CLASS_NAME,"submit-button.btn_action")
login_button.click()

base.selenium_stop()