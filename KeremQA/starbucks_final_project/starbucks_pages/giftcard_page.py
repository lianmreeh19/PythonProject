from selenium.webdriver.common.by import By

class GiftCardPage():
    def __init__(self, driver):
        self.driver = driver

    def get_gift_cards_amount(self):
        print("Check GiftCards amount")
        gift_cards = self.driver.find_elements(By. CSS_SELECTOR, "a[data-product-type='Gift Card'")
        gift_cards_amount = len(gift_cards)
        return gift_cards_amount