from datetime import datetime
import pytest

from page_objects.account_home_page import AccountHomePage
from page_objects.home_page import HomePage


@pytest.mark.usefixtures("setup_and_teardown", "log_on_failure")
class BaseTest:
    # base test added as a base for all tests using common reusable functions & fixtures
    def generate_mail(self):
        cur_time = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        return f"test_ash_{cur_time}@gmail.com"

    def login_in_to_valid_acc(self, username, pswd):
        """login to your valid account"""
        home_page = HomePage(self.driver)
        return home_page.login_to_account(username, pswd)

    def empty_cart_items(self, product_name):
        """to make sure cart is empty before fresh addition"""
        account_home_page = AccountHomePage(self.driver)

        # min 1 product is added in order to avoid empty cart before removal
        product_specific_page = account_home_page.click_on_specific_product(product_name)
        cart_page = product_specific_page.add_product_to_cart_and_go_to_cart_page()

        # now cart items are removed
        cart_page.empty_cart_items()

    def add_products_to_cart(self, *args):
        """new products are added now"""
        account_home_page = AccountHomePage(self.driver)
        for item in args:
            # click on specific product then add it to cart & finally go to home page
            account_home_page.click_on_specific_product(item).add_product_to_cart_and_go_to_home_page()
