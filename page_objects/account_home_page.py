import time

from page_objects.base_page import BasePage
from page_objects.cart_page import CartPage
from page_objects.product_specific_page import ProductSpecificPage


class AccountHomePage(BasePage):
    """
       Represents the account home page and provides methods for interacting with its elements.
    """
    def __init__(self, driver):
        super().__init__(driver)

    logout_btn_id = {'id': "logout2"}
    cart_btn_id = {"id": "cartur"}
    prod_btn_link_txt = {"link_text": "product_name"}

    def confirm_account_login(self):
        return self.get_element_text(self.logout_btn_id)

    def click_on_cart_btn(self):
        self.explicit_wait(self.logout_btn_id, 'element_to_be_clickable')
        self.element_click(self.cart_btn_id)
        return CartPage(self.driver)

    def click_on_specific_product(self, product_name):
        self.prod_btn_link_txt["link_text"] = product_name
        self.explicit_wait(self.logout_btn_id, 'element_to_be_clickable')
        self.element_click(self.prod_btn_link_txt)
        return ProductSpecificPage(self.driver)





