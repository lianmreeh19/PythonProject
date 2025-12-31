from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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

price = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, "inventory_item_price")))
price_text=price.text
print (F"price_text: {price_text}")
base.selenium_stop()