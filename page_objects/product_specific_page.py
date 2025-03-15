from page_objects.base_page import BasePage
from page_objects.cart_page import CartPage


class ProductSpecificPage(BasePage):
    """
       Represents the product specific page of each product and provides methods for interacting with its elements.
    """
    def __init__(self, driver):
        super().__init__(driver)

    addtocart_btn_link_txt = {"link_text": "Add to cart"}
    cart_btn_id = {"id": "cartur"}
    home_btn_xpath = {'xpath': "//div[@class='navbar-collapse']//a[contains(text(), 'Home')]"}

    def click_on_add_to_cart_btn(self):
        self.element_click(self.addtocart_btn_link_txt)
        self.accept_alert()

    def click_on_cart_btn(self):
        self.element_click(self.cart_btn_id)
        return CartPage(self.driver)

    def click_on_home_btn(self):
        self.element_click(self.home_btn_xpath)

    # higher level actions
    def add_product_to_cart_and_go_to_cart_page(self):
        self.click_on_add_to_cart_btn()
        return self.click_on_cart_btn()

    def add_product_to_cart_and_go_to_home_page(self):
        self.click_on_add_to_cart_btn()
        self.click_on_home_btn()

