import logging
import pytest
from page_objects.home_page import HomePage
from tests.base_test import BaseTest


@pytest.mark.order(1)
class TestRegister(BaseTest):
    def test_register_with_all_fields(self):
        logging.info("TestRegister--> test_register_with_all_fields started")

        expected_alert_msg = 'Sign up successful.'
        home_page = HomePage(self.driver)
        alert_text = home_page.register_account(self.generate_mail(), 'asdfg')
        assert alert_text == expected_alert_msg, 'registration failed'

        logging.info("TestRegister--> test_register_with_all_fields completed\n")

    def test_register_with_existing_user(self):
        logging.info("TestRegister--> test_register_with_existing_user started")

        expected_alert_msg = 'This user already exist.'
        home_page = HomePage(self.driver)
        alert_text = home_page.register_account('test_ash1', 'asdfg')
        assert alert_text == expected_alert_msg, 'improper error msg for existing user registration'

        logging.info("TestRegister--> test_register_with_existing_user completed\n")

    def test_register_without_anyfields(self):
        logging.info("TestRegister--> test_register_without_anyfields started")

        expected_alert_msg = 'Please fill out Username and Password.'
        home_page = HomePage(self.driver)
        alert_text = home_page.register_account('', '')
        assert alert_text == expected_alert_msg, 'registering without any fields ' \
                                                 'giving improper error msg'

        logging.info("TestRegister--> test_register_without_anyfields completed\n")

    def test_register_without_username(self):
        logging.info("TestRegister--> test_register_without_username started")

        expected_alert_msg = 'Please fill out Username and Password.'
        home_page = HomePage(self.driver)
        alert_text = home_page.register_account('', 'asdfg')
        assert alert_text == expected_alert_msg, 'registering without username giving ' \
                                                 'improper error msg'

        logging.info("TestRegister--> test_register_without_username completed\n")

    def test_register_without_password(self):
        logging.info("TestRegister--> test_register_without_password started")

        expected_alert_msg = 'Please fill out Username and Password.'
        home_page = HomePage(self.driver)
        alert_text = home_page.register_account(self.generate_mail(), '')
        assert alert_text == expected_alert_msg, 'registering without password ' \
                                                 'giving improper error msg'

        logging.info("TestRegister--> test_register_without_password completed\n")
