import re
import time

from selenium.common import StaleElementReferenceException, TimeoutException

from page_objects.base_page import BasePage


class CartPage(BasePage):
    """
       Represents the cart page of each product and provides methods for interacting with its elements.
    """
    def __init__(self, driver):
        super().__init__(driver)

    product_name_xpath = {'xpath': "//table[contains(@class, 'table-bordered')]//td[2]"}
    product_price_xpath = {'xpath': "//table[contains(@class, 'table-bordered')]//td[3]"}
    product_delete_btn_xpath = {'xpath': "//table[contains(@class, 'table-bordered')]//tr[1]//a"}
    product_delete_total_btns_xpath = {'xpath': "//table[contains(@class, 'table-bordered')]//a"}
    home_btn_xpath = {'xpath': "//div[@class='navbar-collapse']//a[text()='Home ']"}

    total_amt_txt_id = {'id': "totalp"}
    placeorder_btn_xpath = {'xpath': "//button[text()='Place Order']"}
    name_field_id = {'id': 'name'}
    country_field_id = {'id': 'country'}
    city_field_id = {'id': 'city'}
    card_field_id = {'id': 'card'}
    month_field_id = {'id': 'month'}
    year_field_id = {'id': 'year'}
    purchase_btn_xpath = {'xpath': "//button[text()='Purchase']"}
    purchase_confirm_txt_xpath = {'xpath': "//div[contains(@class, 'sweet-alert')]/h2"}
    purchased_info_txt_xpath = {'xpath': "//p[@class='lead text-muted ']"}
    purchase_confirm_ok_btn_xpath = {'xpath': "//div[contains(@class, 'sweet-alert')]//button[text()='OK']"}

    def get_first_product_name_in_cart(self):
        return self.get_element_text(self.product_name_xpath)

    def get_total_cart_amount(self):
        return int(self.get_element_text(self.total_amt_txt_id))

    def click_on_place_order(self):
        self.element_click(self.placeorder_btn_xpath)

    def empty_cart_items(self):
        self.explicit_wait(self.product_price_xpath, 'element_to_be_clickable')
        prev_count_of_del_btns = self.get_elements_count(self.product_delete_total_btns_xpath)
        while True:
            try:
                # count of current no of delete buttons becomes 0 only if its really 0 or during page reload so,
                # we track previous count of delete buttons
                if self.get_elements_count(self.product_delete_total_btns_xpath) > 0:
                    prev_count_of_del_btns = self.get_elements_count(self.product_delete_total_btns_xpath)
                    self.element_click(self.product_delete_btn_xpath)
                elif prev_count_of_del_btns > 1:
                    self.explicit_wait(self.product_price_xpath, 'element_to_be_clickable')
                    prev_count_of_del_btns -= 1
                else:
                    break
            except StaleElementReferenceException:
                continue
            except TimeoutException:
                break
        self.element_click(self.home_btn_xpath)

    # high level actions
    def purchase_cart_items(self, purchase_info: dict):
        self.explicit_wait(self.product_price_xpath, 'element_to_be_clickable')  # wait for product to load
        self.click_on_place_order()
        self.type_into_element(purchase_info['name'], self.name_field_id)   # enter name
        self.type_into_element(purchase_info['country'], self.country_field_id)   # enter country
        self.type_into_element(purchase_info['city'], self.city_field_id)   # enter city
        self.type_into_element(purchase_info['credit_card'], self.card_field_id)  # enter credit card no
        self.type_into_element(purchase_info['month'], self.month_field_id)   # enter month
        self.type_into_element(purchase_info['year'], self.year_field_id)    # enter year
        self.element_click(self.purchase_btn_xpath)  # click on purchase button
        purchase_confirm_msg = self.get_element_text(self.purchase_confirm_txt_xpath)

        # to get amount in purchased info
        purchased_txt_info = self.get_element_text(self.purchased_info_txt_xpath)
        purchased_amount = None
        match = re.search(r"Amount:\s*(\d+)", purchased_txt_info)
        if match:
            purchased_amount = int(match.group(1))
        self.element_click(self.purchase_confirm_ok_btn_xpath)  # click on ok button
        return purchase_confirm_msg, purchased_amount


