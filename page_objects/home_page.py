import logging
import time

from selenium.common import NoAlertPresentException

from page_objects.account_home_page import AccountHomePage
from page_objects.base_page import BasePage


class HomePage(BasePage):
    """
       Represents the home page and provides methods for interacting with its elements.
    """

    def __init__(self, driver):
        super().__init__(driver)

    sign_up_btn_id = {"id": "signin2"}
    signup_username_field_id = {"id": "sign-username"}
    signup_password_field_id = {"id": "sign-password"}
    signup_form_btn_xpath = {'xpath': "//button[@onclick='register()']"}

    login_btn_id = {"id": "login2"}
    login_username_field_id = {"id": "loginusername"}
    login_password_field_id = {"id": "loginpassword"}
    login_form_btn_xpath = {'xpath': "//button[@onclick='logIn()']"}


    def click_on_sign_up_btn(self):
        self.element_click(self.sign_up_btn_id)

    def enter_username_in_signup_form(self, username):
        self.type_into_element(username, self.signup_username_field_id)

    def enter_password_in_signup_form(self, password):
        self.type_into_element(password, self.signup_password_field_id)

    def click_on_signup_form_btn(self):
        self.element_click(self.signup_form_btn_xpath)

    def click_on_login_btn(self):
        self.element_click(self.login_btn_id)

    def enter_username_in_login_form(self, username):
        self.type_into_element(username, self.login_username_field_id)

    def enter_password_in_login_form(self, password):
        self.type_into_element(password, self.login_password_field_id)

    def click_on_login_form_btn(self):
        self.element_click(self.login_form_btn_xpath)

    # higher level actions
    def register_account(self, username, password):
        self.click_on_sign_up_btn()
        self.enter_username_in_signup_form(username)
        self.enter_password_in_signup_form(password)
        self.click_on_signup_form_btn()
        return self.get_alert_text()

    def login_to_account(self, username, password):
        self.click_on_login_btn()
        self.enter_username_in_login_form(username)
        self.enter_password_in_login_form(password)
        self.click_on_login_form_btn()
        return AccountHomePage(self.driver)

    def login_to_account_failure(self, username, password):
        self.click_on_login_btn()
        self.enter_username_in_login_form(username)
        self.enter_password_in_login_form(password)
        self.click_on_login_form_btn()
        return self.get_alert_text()
