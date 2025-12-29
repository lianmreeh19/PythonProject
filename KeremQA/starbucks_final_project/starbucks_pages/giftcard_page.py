from selenium.webdriver.common.by import By


class GiftCardPage():
    def __init__(self, driver):
        self.driver = driver

    def check_if_giftcard_exists_and_click_on_it(self):
        print('Check if GiftCard exists and click on it')
        thank_you_giftcard = self.driver.find_element(By. CSS_SELECTOR, "a[class='block base___Vxsau'").text
        return thank_you_giftcard