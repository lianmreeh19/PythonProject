import time
from time import sleep
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver
from KeremQA.selenium_example.seleniumBaseKerem import seleniumBaseKerem

base = seleniumBaseKerem()
driver = base.selenium_start_with_url("https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login")
elements = driver.find_elements(By.CLASS_NAME, "btn.btn-primary.btn-lg")
bank_manager_login = elements[1]
bank_manager_login.click()

base.selenium_stop()