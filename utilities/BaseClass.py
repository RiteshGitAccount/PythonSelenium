import logging
import os.path
import time
from traceback import print_stack

import allure
from allure_commons.types import AttachmentType
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.CustomeLogger import custom_logger
from utilities.ExcelReader import read_excel_data, write_excel_data


class BaseClass:
    log = custom_logger(logging.DEBUG)
    data_excel_file_path = None
    env_file_path = None
    env_data = None
    conf_file_path = None
    conf_data = None

    def __init__(self, driver):
        self.driver = driver
        self.input_data = None

    def load_url(self, urls):
        self.driver.get(urls)

    def read_excel_data(self, sheet_name, col_row):
        return read_excel_data(self.data_excel_file_path, sheet_name, col_row)

    def write_excel_data(self, sheet_name, col_row, data):
        return write_excel_data(self.data_excel_file_path, sheet_name, col_row, data)

    def print_log(self, print_statement, log_type="info"):
        if log_type == "info":
            self.log.info(print_statement)
        elif log_type == "warn":
            self.log.warn(print_statement)
        elif log_type == "debug":
            self.log.debug(print_statement)
        elif log_type == "error":
            self.log.error(print_statement)
        print(print_statement)

    def screenshots(self, result_message, allure_name="Screenshot"):
        allure.attach(self.driver.get_screenshot_as_png(), name=allure_name, attachment_type=AttachmentType.PNG)

        file_name = result_message + "-" + str(round(time.time() * 1000)) + ".png"
        screenshot_dir = "../screenshots/"
        relative_file_name = screenshot_dir + file_name
        current_dir = os.path.dirname(__file__)
        destination_file = os.path.join(current_dir, relative_file_name)
        destination_dir = os.path.join(current_dir, screenshot_dir)

        try:
            if not os.path.exists(destination_dir):
                os.makedirs(destination_dir)
            self.driver.save_screenshot(destination_file)
            self.print_log(f"Screenshot saved to dir: {destination_dir}")
        except:
            self.print_log("Exception occurred while taking screenshot", log_type="error")
            print_stack()

    def get_by_type(self, locator_type):

        locator_type = locator_type.lower()
        if locator_type == "id":
            return By.ID
        elif locator_type == "name":
            return By.NAME
        elif locator_type == "tag":
            return By.TAG_NAME
        elif locator_type == "css":
            return By.CSS_SELECTOR
        elif locator_type == "class":
            return By.CLASS_NAME
        elif locator_type == "xpath":
            return By.XPATH
        elif locator_type == "link" or locator_type == "link_text":
            return By.LINK_TEXT
        elif locator_type == "par_link" or locator_type == "par_link_text":
            return By.PARTIAL_LINK_TEXT
        else:
            self.print_log(f"Locator type- '{locator_type}' not correct/supported", log_type="error")
            return False

    def get_element(self, locator, locator_type="xpath"):
        element = None
        try:
            by_type = self.get_by_type(locator_type)
            element = self.driver.find_element(by_type, locator)
        except:
            self.screenshots(f"Element issue", allure_name="Element issue")
            self.print_log(f"Element not fount with locator: '{locator}' and locator_type: '{locator_type}'",log_type="error")
        assert element is not None
        return element

    def wait_for_element_visibility(self, locator, locator_type="xpath", timeout=10, poll_frequency=1):
        element = None
        try:
            by_type = self.get_by_type(locator_type)
            wait = WebDriverWait(self.driver, timeout=timeout,
                                 poll_frequency=poll_frequency,
                                 ignored_exceptions=[NoSuchElementException, ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.visibility_of_element_located((by_type, locator)))
        except:
            self.screenshots(f"Element not visible", allure_name="Element not visible")
            self.print_log(
                f"Element not appeared on the web page with locator: '{locator}' - locator_type: '{locator_type}' within '{timeout}' seconds",
                log_type="error")
        assert element is not None

    def wait_for_element_invisibility(self, locator, locator_type="xpath", timeout=10, poll_frequency=1):
        element = None
        try:
            by_type = self.get_by_type(locator_type)
            wait = WebDriverWait(self.driver, timeout=timeout,
                                 poll_frequency=poll_frequency)
            element = wait.until(EC.invisibility_of_element((by_type, locator)))
        except:
            self.screenshots(f"Element is visible", allure_name="Element is visible")
            self.print_log(
                f"Element is still visible on the web page with locator: '{locator}' - locator_type: '{locator_type}' within '{timeout}' seconds",
                log_type="error")
        assert element is True

    def click_element(self, locator, locator_type="xpath"):
        element = None
        try:
            if locator:
                element = self.get_element(locator, locator_type)
                assert element is not None
                element.click()
        except:
            self.print_log(f"Can not click on the element with locator: '{locator}' - locator_type: '{locator_type}'")
            print_stack()
            assert element is not None

    def send_text(self, data, locator, locator_type="xpath"):
        element = None
        try:
            if locator:
                element = self.get_element(locator, locator_type)
                assert element is not None
                element.clear()
                element.send_keys(data)
        except:
            self.print_log(f"Can not click on the element with locator: '{locator}' - locator_type: '{locator_type}'")
            print_stack()
            assert element is not None
