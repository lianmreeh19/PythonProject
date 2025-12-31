from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class seleniumBaseStarbucks():

    def selenium_start_with_url(self, url):
        print("test start")
        options = Options()
        options.add_argument("--incognito")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        self.driver = webdriver.Chrome(options=options)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get(url)
        return self.driver

    def selenium_stop(self):
        print("*******test stop*******")
        self.driver.close()
