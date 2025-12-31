from KeremQA.starbucks_final_project.locators import GiftCardPageLocators


class GiftCardPage():
    def __init__(self, driver):
        self.driver = driver

    def get_gift_cards_amount(self):
        print("Check GiftCards amount")
        gift_cards = self.driver.find_elements(*GiftCardPageLocators.GIFT_CARDS)
        gift_cards_amount = len(gift_cards)
        return gift_cards_amount
