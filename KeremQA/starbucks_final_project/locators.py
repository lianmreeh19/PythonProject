from selenium.webdriver.common.by import By
from KeremQA.starbucks_final_project.globals import REWARDS_BUTTON, HOME_PAGE_BUTTON, START_AN_ORDER_BUTTON, \
    GIFT_CARD_BUTTON, FIND_A_STORE_BUTTON

class WelcomePageLocators(object):
    COOKIES_AGREE_BUTTON_LOCATOR = By.ID, "truste-consent-button"

    REWARDS_BUTTON_LOCATOR = By.LINK_TEXT, REWARDS_BUTTON
    HOME_PAGE_BUTTON_LOCATOR = By.CLASS_NAME, HOME_PAGE_BUTTON
    START_AN_ORDER_BUTTON_LOCATOR = By.LINK_TEXT, START_AN_ORDER_BUTTON

    GIFT_CARD_BUTTON_LOCATOR = By.PARTIAL_LINK_TEXT, GIFT_CARD_BUTTON

    EXIST_BUTTONS_LOCATOR = By.CLASS_NAME, "sb-globalNav__desktopLink.inline-block.text-noUnderline.text-xxs.text-upper.text-bold"

    FIND_A_STORE_BUTTON_LOCATOR = By.PARTIAL_LINK_TEXT, FIND_A_STORE_BUTTON

class ProductOrderPageLocators(object):
    DRINK_CATEGORY_TEXT_LOCATOR = By.CLASS_NAME, "sb-heading.text-md.pb3.text-bold"

    TEXT_DRINK_LOCATOR = By.CSS_SELECTOR, "a[href='/menu/product/28498/iced']"

    ESPRESSO_TYPE_LOCATOR = By.ID, "41-modifier-select"

    ADD_TO_ORDER_BUTTON_LOCATOR = By.CSS_SELECTOR, "button[data-e2e='add-to-order-button']"

    JUST_BROWSING_BUTTON_LOCATOR = By.CSS_SELECTOR, "button[type='button']"

    SIGN_IN_PAGE_LOCATOR = By.CSS_SELECTOR, "div[class='sb-contentColumn__inner']"

class GiftCardPageLocators(object):
    GIFT_CARDS = By.CSS_SELECTOR, "a[data-product-type='Gift Card']"

class FindAStorePageLocators(object):
    NEW_YORK_STORE_LOCATOR = By.NAME, "place"

    NEW_YORK_STORE_TEXT_LOCATOR = By.CLASS_NAME, "flex.justify-between.content___DiNrm"





