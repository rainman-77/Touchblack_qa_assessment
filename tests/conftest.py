import logging
import os
import allure
import pytest
from allure_commons.types import AttachmentType
from configurations import read_configurations as rc
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions

global driver


def pytest_configure(config):       # log settings
    # log file for the standalone test
    os.makedirs("logs", exist_ok=True)  # create log folder if its not present
    log_file = "logs/assessment_test.log"   # log file path

    # Configure logging
    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        datefmt="%m/%d/%Y %I:%M:%S %p",
    )
    logging.info(".....Starting the standalone test setup...")


@pytest.fixture()
def log_on_failure(request):        # this creates screenshot on test failure in allure report
    global driver
    yield
    item = request.node     # for allure reporting
    if item.rep_call.failed:    # takes screenshots only for failed test case & attaches to allure
        allure.attach(driver.get_screenshot_as_png(), name="failed_test", attachment_type=AttachmentType.PNG)


@pytest.hookimpl(hookwrapper=True, tryfirst=True)   # for allure reporting
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture()
def setup_and_teardown(request):
    global driver
    browser = None
    options = None
    browser_mode = rc.read_configuration("basic info", "browser_mode")

    browser = rc.read_configuration("basic info", "browser")  # uses config.ini to get specific browser instance
    logging.info(f"Running test in '{browser_mode}-Standalone' mode on '{browser}' browser in local environment")

    if browser == 'chrome':
        options = ChromeOptions()
        if browser_mode == 'headless':  # now added headless test here
            options.add_argument("--headless")
        driver = webdriver.Chrome(options=options)

    elif browser == 'firefox':
        options = FirefoxOptions()
        if browser_mode == 'headless':
            options.add_argument("--headless")
        driver = webdriver.Firefox(options=options)

    elif browser == 'edge':
        options = EdgeOptions()
        if browser_mode == 'headless':
            options.add_argument("--headless")
        driver = webdriver.Edge(options=options)

    else:
        raise ValueError("provide valid browser name in config.ini file")

    driver.maximize_window()
    url = rc.read_configuration("basic info", "url")
    driver.get(url)
    request.cls.driver = driver
    yield
    driver.quit()
