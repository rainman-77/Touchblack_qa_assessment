import logging
import pytest
from tests.base_test import BaseTest


@pytest.mark.order(3)
class TestCart(BaseTest):
    # credentials for valid login
    username = 'test_ash1'
    pswd = 'asdfg'

    def test_product_added_to_cart(self):
        logging.info("TestCart--> test_product_added_to_cart started")

        product_name = 'Samsung galaxy s7'

        account_home_page = self.login_in_to_valid_acc(self.username, self.pswd)  # login in to your account

        self.empty_cart_items(product_name)  # to make sure cart is empty before fresh addition

        # click on specific product then add it to cart & finally go to cart page
        product_specific_page = account_home_page.click_on_specific_product(product_name)
        cart_page = product_specific_page.add_product_to_cart_and_go_to_cart_page()

        # compare product name in cart with expected product name
        assert cart_page.get_first_product_name_in_cart().__eq__(product_name)

        logging.info("TestCart--> test_product_added_to_cart completed\n")

    def test_total_product_cost_added_to_cart(self):
        logging.info("TestCart--> test_total_product_cost_added_to_cart started")

        product_name1 = 'Samsung galaxy s7'
        product_name2 = 'Samsung galaxy s6'
        total_expected_amount = 1160

        account_home_page = self.login_in_to_valid_acc(self.username, self.pswd)  # login in to your account

        self.empty_cart_items(product_name1)  # to make sure cart is empty before fresh addition
        self.add_products_to_cart(product_name1, product_name2)  # new products are added now

        # go to cart & get total amount
        cart_page = account_home_page.click_on_cart_btn()
        assert cart_page.get_total_cart_amount() == total_expected_amount

        logging.info("TestCart--> test_total_product_cost_added_to_cart completed\n")

    def test_purchase_of_a_product(self):
        logging.info("TestCart--> test_purchase_of_a_product started")

        product_name = 'Samsung galaxy s7'
        expected_purchase_amount = 800
        expected_purchase_confirm_msg = 'Thank you for your purchase!'
        purchase_info = {'name': 'test_ash', 'country': 'India', 'city': 'Shimoga',
                         'credit_card': '4354354523', 'month': 'feb', 'year': '2027'}

        account_home_page = self.login_in_to_valid_acc(self.username, self.pswd)  # login in to your account

        self.empty_cart_items(product_name)  # to make sure cart is empty before fresh addition

        # click on specific product then add it to cart & finally go to cart page
        product_specific_page = account_home_page.click_on_specific_product(product_name)
        cart_page = product_specific_page.add_product_to_cart_and_go_to_cart_page()

        # purchase cart items
        purchased_confirm_msg, purchased_amount = cart_page.purchase_cart_items(purchase_info)
        assert purchased_confirm_msg == expected_purchase_confirm_msg, "purchase confirmation message isn't mathing"
        assert purchased_amount == expected_purchase_amount

        logging.info("TestCart--> test_purchase_of_a_product completed\n")
