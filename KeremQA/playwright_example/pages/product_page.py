from playwright.sync_api import Page


class productPage():
    def __init__(self, page):
        self.page = page

    def verify_and_get_prices(self):
        prices = self.page.query_selector_all("[class='inventory_item_price']")
        prices_as_text = []
        for price in prices:
            price_as_str = price.text_content()
            print(price_as_str)
            price_as_str = price_as_str.replace("$","")
            price_as_float = float(price_as_str)
            is_pass = price_as_float < 100
            assert is_pass, "the price is more than 100$"
            prices_as_text.append(price_as_str)
            print("the price is lower than 100$")
        return prices_as_text