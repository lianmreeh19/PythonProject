from selenium.webdriver.common.by import By


class GiftCardPage():
    def __init__(self, driver):
        self.driver = driver

    def get_giftcards_amount(self):
        print('Check GiftCards amount')
        giftcards = self.driver.find_elements(By. CSS_SELECTOR, "a[data-product-type='Gift Card'")
        giftcards_amount = len(giftcards)
        return giftcards_amount