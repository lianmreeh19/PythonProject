from selenium.webdriver.common.by import By


class LoginPage():
    def __init__(self, driver):
        self.driver = driver

    def click_on_login_button(self):
        print("click_on_login_button")
        self.driver.find_element(By.ID, "login-button").click()

    def set_user_and_password(self, user_text, password_text):
        self.driver.find_element(By.ID, "user-name").send_keys(user_text)
        self.driver.find_element(By.ID, "password").send_keys(password_text)