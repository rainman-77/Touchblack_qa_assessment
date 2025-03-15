import logging
import pytest
from configurations import excel_utils
from page_objects.home_page import HomePage
from tests.base_test import BaseTest


@pytest.mark.order(2)
class TestLogin(BaseTest):
    @pytest.mark.parametrize("email, psw", excel_utils.get_all_excel_data("login_test"))  # data driven testing
    def test_login_with_valid_cred(self, email, psw):
        logging.info(f"TestLogin--> test_login_with_valid_cred started for {email}")

        home_page = HomePage(self.driver)
        account_home_page = home_page.login_to_account(email, psw)
        logout_button_name = 'Log out'
        assert account_home_page.confirm_account_login().__eq__(logout_button_name)

        logging.info(f"TestLogin--> test_login_with_valid_cred completed for {email}\n")

    def test_login_invalid_username_and_valid_password(self):
        logging.info("TestLogin--> test_login_invalid_username_and_valid_password started")

        home_page = HomePage(self.driver)
        alert_text = home_page.login_to_account_failure('wrew%45', 'asdfg')
        assert alert_text == 'User does not exist.', 'improper error msg for logging in with ' \
                                                     'invalid username & valid password'

        logging.info("TestLogin--> test_login_invalid_username_and_valid_password completed\n")

    def test_login_valid_username_and_invalid_password(self):
        logging.info("TestLogin--> test_login_valid_username_and_invalid_password started")

        home_page = HomePage(self.driver)
        alert_text = home_page.login_to_account_failure('test_ash1', '23423ertre')
        assert alert_text == 'Wrong password.', 'improper error msg for logging in with ' \
                                                'valid username & invalid password'

        logging.info("TestLogin--> test_login_valid_username_and_invalid_password completed\n")

    def test_login_without_cred(self):
        logging.info("TestLogin--> test_login_without_cred started")

        home_page = HomePage(self.driver)
        alert_text = home_page.login_to_account_failure('', '')
        assert alert_text == 'Please fill out Username and Password.', 'improper error msg for logging in with ' \
                                                                       'empty fields'

        logging.info("TestLogin--> test_login_without_cred completed\n")
