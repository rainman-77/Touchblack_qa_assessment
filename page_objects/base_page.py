import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    """
      A base class for reusable Selenium utilities.
      Provides methods for waiting on elements and common web interactions.
    """
    def __init__(self, driver):
        self.driver = driver

    default_timeout = 10

    def wait_for_condition(self, locator, condition):
        wait = WebDriverWait(self.driver, self.default_timeout)
        for loc_type, loc_value in locator.items():
            if loc_type == "id":
                return wait.until(condition((By.ID, loc_value)))
            elif loc_type == "name":
                return wait.until(condition((By.NAME, loc_value)))
            elif loc_type == "class_name":
                return wait.until(condition((By.CLASS_NAME, loc_value)))
            elif loc_type == "link_text":
                return wait.until(condition((By.LINK_TEXT, loc_value)))
            elif loc_type == "xpath":
                return wait.until(condition((By.XPATH, loc_value)))
            elif loc_type == "css":
                return wait.until(condition((By.CSS_SELECTOR, loc_value)))

    def explicit_wait(self, locator, wait_condition):
        condition = getattr(ec, wait_condition)
        return self.wait_for_condition(locator, condition)

    def explicit_wait_for_elements(self, locator):
        return self.wait_for_condition(locator, ec.presence_of_all_elements_located)

    def get_element(self, locator):
        element = None
        for loc_type, loc_value in locator.items():     # get locator dictionary's key-value pairs one at a time
            if "id" in loc_type:
                element = self.driver.find_element(By.ID, loc_value)
            elif "name" in loc_type:
                element = self.driver.find_element(By.NAME, loc_value)
            elif "class_name" in loc_type:
                element = self.driver.find_element(By.CLASS_NAME, loc_value)
            elif "link_text" in loc_type:
                element = self.driver.find_element(By.LINK_TEXT, loc_value)
            elif "xpath" in loc_type:
                element = self.driver.find_element(By.XPATH, loc_value)
            elif "css" in loc_type:
                element = self.driver.find_element(By.CSS_SELECTOR, loc_value)
        return element

    def get_elements(self, locator):
        elements = []
        for loc_type, loc_value in locator.items():
            if "id" in loc_type:
                elements = self.driver.find_elements(By.ID, loc_value)
            elif "name" in loc_type:
                elements = self.driver.find_elements(By.NAME, loc_value)
            elif "class_name" in loc_type:
                elements = self.driver.find_elements(By.CLASS_NAME, loc_value)
            elif "link_text" in loc_type:
                elements = self.driver.find_elements(By.LINK_TEXT, loc_value)
            elif "xpath" in loc_type:
                elements = self.driver.find_elements(By.XPATH, loc_value)
            elif "css" in loc_type:
                elements = self.driver.find_elements(By.CSS_SELECTOR, loc_value)
        return elements

    def type_into_element(self, text, locator, wait_condition='visibility_of_element_located'):
        element = self.explicit_wait(locator, wait_condition)
        element.click()
        element.clear()
        element.send_keys(text)

    def type_into_elements(self, text, locator, index=0):
        self.explicit_wait_for_elements(locator)
        elements = self.get_elements(locator)
        if elements and index < len(elements):
            elements[index].click()
            elements[index].clear()
            elements[index].send_keys(text)
        else:
            raise IndexError(f"No element found at index {index}")

    def get_element_text(self, locator, wait_condition='visibility_of_element_located'):
        element = self.explicit_wait(locator, wait_condition)
        return element.text

    def get_elements_text_by_index(self, locator, index=0):
        self.explicit_wait_for_elements(locator)
        elements = self.get_elements(locator)
        if elements and index < len(elements):
            return elements[index].text
        else:
            raise IndexError(f"No element found at index {index}")

    def element_click(self, locator, wait_condition='visibility_of_element_located'):
        element = self.explicit_wait(locator, wait_condition)
        element.click()

    def elements_click_by_index(self, locator, index=0):
        self.explicit_wait_for_elements(locator)
        elements = self.get_elements(locator)
        if elements and index < len(elements):
            elements[index].click()
        else:
            raise IndexError(f"No element found at index {index}")

    def get_elements_count(self, locator):
        try:
            # self.explicit_wait_for_elements(locator)
            elements = self.get_elements(locator)
            return len(elements)
        except Exception as e:
            logging.error(f"Unable to retrieve elements count for locator: {locator}. Exception: {e}")
            return 0  # Return 0 if no elements are found or another issue occurs

    def get_alert_text(self):
        wait = WebDriverWait(self.driver, self.default_timeout)
        wait.until(ec.alert_is_present())
        info_alert = self.driver.switch_to.alert
        info_alert_text = info_alert.text
        info_alert.accept()
        return info_alert_text

    def accept_alert(self):
        wait = WebDriverWait(self.driver, self.default_timeout)
        wait.until(ec.alert_is_present())
        info_alert = self.driver.switch_to.alert
        info_alert.accept()
