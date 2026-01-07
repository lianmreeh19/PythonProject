class testProductPage():
    def test_product_price(self, setup_swaglabs):
        page, login_page = setup_swaglabs
        login_page.login("standard_user", "fake")
