import time
from time import sleep

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver
class seleniumBaseKerem():
    def selenium_start(self):
        print("Test start")
        service = ChromeService(executable_path=ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        driver.maximize_window()
        driver.implicitly_wait(10)
        return driver

    def selenium_start_with_url(self, url):
        print("test start")
        service = ChromeService(executable_path=ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get(url)
        return self.driver

    def selenium_stop(self):
        print("test stop")
        self.driver.close()

    def click_on_element(self, element):
        print("test click on element")
        is_selected = element.is_selected()
        if is_selected == False:
            element.click()
        after = element.is_selected()
        return after

    def click_and_assert_on_element(self, element):
        print("test click on element")
        is_selected = element.is_selected()
        if is_selected == False:
            element.click()
        after = element.is_selected()
        assert after == True , "After clicking on element, it didn't worked as expected"
        return after
