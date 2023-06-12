import logging
import os.path
import time
from traceback import print_stack

from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select

import allure
from allure_commons.types import AttachmentType
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import utilities.CustomeLogger as cl


class BaseClass:
    log = cl.custom_logger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver

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
            self.print_log(f"Locator type {locator_type} not correct/supported", log_type="error")
            return False

    def get_element(self, locator, locator_type="xpath"):
        element = None
        try:
            by_type = self.get_by_type(locator_type)
            element = self.driver.find_element(by_type, locator)
        except:
            self.screenshots(f"Element issue", allure_name="Element issue")
            self.print_log(f"Element not fount with locator: {locator} and locator_type: {locator_type}")
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
                f"Element not appeared on the web page with locator: {locator} - locator_type: {locator_type} within {timeout} seconds",
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
                f"Element is still visible on the web page with locator: {locator} - locator_type: {locator_type} within {timeout} seconds",
                log_type="error")
        assert element is True

    # Mouse and Keyboard Actions
    def click_element(self, locator, locator_type="xpath"):
        element = None
        try:
            if locator:
                element = self.get_element(locator, locator_type)
                assert element is not None
                element.click()
        except:
            self.print_log(f"Can not click on the element with locator: {locator} - locator_type: {locator_type}")
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
            self.print_log(f"Can not enter text in element with locator: {locator} - locator_type: {locator_type}")
            print_stack()
            assert element is not None

    def verify_text(self, data, locator, locator_type="xpath"):
        element = None
        try:
            if locator:
                element = self.get_element(locator, locator_type)
                assert element is not None
                assert element.text == data
        except:
            self.print_log(
                f"Cannot find text / attribute (value) of element with locator: {locator} - locator_type: {locator_type}")
            print_stack()
            assert element is not None

    def double_click(self, locator, locator_type="xpath"):
        element = None
        try:
            if locator:
                element = self.get_element(locator, locator_type)
                assert element is not None
                action = ActionChains(self.driver)
                action.double_click(element).perform()
        except:
            self.print_log(f"Cannot double click on element with locator: {locator} - locator_type: {locator_type}")
            print_stack()
            assert element is not None

    def context_click(self, locator, locator_type="xpath"):
        element = None
        try:
            if locator:
                element = self.get_element(locator, locator_type)
                assert element is not None
                action = ActionChains(self.driver)
                action.context_click(element).perform()
        except:
            self.print_log(f"Cannot right click on element with locator: {locator} - locator_type: {locator_type}")
            print_stack()
            assert element is not None

    def move_to_element(self, locator, locator_type="xpath"):
        element = None
        try:
            if locator:
                element = self.get_element(locator, locator_type)
                assert element is not None
                action = ActionChains(self.driver)
                action.move_to_element(element).perform()
        except:
            self.print_log(f"Cannot move to element with locator: {locator} - locator_type: {locator_type}")
            print_stack()
            assert element is not None

    def move_to_element_with_offset(self, x_offset, y_offset, locator, locator_type="xpath"):
        element = None
        try:
            if locator:
                element = self.get_element(locator, locator_type)
                assert element is not None
                action = ActionChains(self.driver)
                action.move_to_element_with_offset(element, x_offset, y_offset).perform()
        except:
            self.print_log(
                f"Cannot move to element with offset values :{x_offset} , {y_offset} locator: {locator} locator_type:{locator_type}")
            print_stack()
            assert element is not None

    def hover(self, locator, locator_type="xpath"):
        element = None
        try:
            if locator:
                element = self.get_element(locator, locator_type)
                assert element is not None
                action = ActionChains(self.driver)
                action.move_to_element(element).perform()
        except:
            self.print_log(f"Cannot hover on element with locator: {locator} - locator_type: {locator_type}")
            print_stack()
            assert element is not None

    def drag_and_drop(self, source_locator, target_locator, source_locator_type="xpath", target_locator_type="xpath"):
        source_element = None
        target_element = None

        try:
            if locator:
                source_element = self.get_element(source_locator, source_locator_type)
                target_element = self.get_element(target_locator, target_locator_type)
                assert source_element is not None
                assert target_element is not None
                action = ActionChains(self.driver)
                action.drag_and_drop(source_element, target_element).perform()

        except:
            self.print_log(
                f"Cannot drag element from locator: {locator} - locator_type: {locator_type} to target ocator: {locator} - locator_type: {locator_type}")
            print_stack()
            assert element is not None

    def drag_and_drop_by_offset(self, x_offset, y_offset, locator, locator_type="xpath"):
        element = None
        try:
            if locator:
                element = self.get_element(locator, locator_type)
                assert element is not None
                action = ActionChains(self.driver)
                action.drag_and_drop_by_offset(element, x_offset, y_offset).perform()
        except:
            self.print_log(f"Cannot drag and drop with offset for locator: {locator} - locator_type: {locator_type}")
            print_stack()
            assert element is not None

    def drag_and_drop_javascript(self, source, target):  # source & target given as class name in SS - eg: '#coulmn-a'
        file = cwd.split("tests")
        fname = file[0] + "Resources\\drag_and_drop_helper.js"
        print(fname)
        with open(fname, 'r') as js_file:
            line = js_file.readline()
            script = ''
            while line:
                script += line
                line = js_file.readline()

        driver.execute_script(script + "$('" + source + "').simulateDragDrop({ dropTarget: '" + target + "'});")
        time.sleep(2)

    def horizontal_scroll(self, x_offset, y_offset, locator, locator_type="xpath"):
        element = None
        try:
            if locator:
                element = self.get_element(locator, locator_type)
                assert element is not None
                action = ActionChains(self.driver)
                action.click_and_hold(element).move_by_offset(x_offset, y_offset).release().perform()
        except:
            self.print_log(
                f"Cannot scroll horizontally for element with locator: {locator} - locator_type: {locator_type}")
            print_stack()
            assert element is not None

    def is_element_displayed(self, locator, locator_type="xpath"):
        element = None
        try:
            if locator:
                element = self.get_element(locator, locator_type)
                assert element is not None
                return element.is_displayed()
        except:
            self.print_log(f"Element not displayed - locator: {locator} - locator_type: {locator_type}")
            print_stack()
            assert element is not None

    def is_element_selected(self, locator, locator_type="xpath"):
        element = None
        try:
            if locator:
                element = self.get_element(locator, locator_type)
                assert element is not None
                return element.is_selected()
        except:
            self.print_log(f"Element/Check box not selected - locator: {locator} - locator_type: {locator_type}")
            print_stack()
            assert element is not None

    # Browser interactions
    def maximize_browser(self):
        self.driver.maximize_window()

    def get_title(self):
        return self.driver.title

    def minimize_browser(self):
        self.driver.minimize_window()

    def get_url(self):
        return self.driver.current_url

    def resize_browser(self, x, y):
        self.driver.set_window_size(x, y)

    def delete_all_cookies(self, x, y):
        self.driver.delete_all_cookies()

    # Iframes
    def switch_to_iframe(self, locator, locator_type="xpath"):
        element = None
        try:
            if locator:
                element = self.get_element(locator, locator_type)
                assert element is not None
                self.driver.switch_to.frame(element)
        except:
            self.print_log(f"Cannot switch to frame with locator: {locator} - locator_type: {locator_type}")
            print_stack()
            assert element is not None

    def switch_to_default_content(self):
        # element = None
        try:
            # if locator:
            # element = self.get_element(locator, locator_type)
            # assert element is not None
            self.driver.switch_to.default_content()
        except:
            self.print_log(f"Cannot switch back to default window from iFrame")
            print_stack()
            assert element is not None

    # Alerts
    def alert_accept(self):
        try:
            alert = driver.switch_to.alert
            alert.accept
        except:
            self.print_log(f"Not able to accept alert")
            print_stack()

    def alert_dismiss(self):
        try:
            alert = driver.switch_to.alert
            alert.dismiss
        except:
            self.print_log(f"Not able to dismiss alert")
            print_stack()

    def alert_text(self):
        try:
            alert = driver.switch_to.alert
            text = alert.text
            return text
        except:
            self.print_log(f"Not able retrieve text from the alert")
            print_stack()

    # Window Handles

    def get_current_window_handle(self):
        try:
            return driver.current_window_handle
        except:
            self.print_log(f"Not able to retrieve current window handle")
            print_stack()

    def get_all_window_handles(self):
        try:
            handles = driver.window_handles
            return handles
        except:
            self.print_log(f"Not able to retrieve current window handle")
            print_stack()

    def switch_to_window(self, handle_identifier):
        try:
            parent_handle = get_current_window_handle()
            driver.switch_to.window(handle_identifier)

        except:
            self.print_log(f"Not able to switch to window handle")
            print_stack()

    # Drop downs

    def select_dropdown(self, criteria, data, locator, locator_type="xpath"):
        element = None
        try:
            if locator:
                element = self.get_element(locator, locator_type)
                assert element is not None
                sel = Select(element)

                if criteria == "Index":
                    sel.select_by_index(data)
                elif criteria == "Visible Text":
                    sel.select_by_visible_text(data)
                elif criteria == "Value":
                    sel.select_by_value(data)
        except:
            self.print_log(f"Cannot select drop down values based on {criteria} for locator: {locator} - locator_type: {locator_type}")
            print_stack()
            assert element is not None

    def deselect_dropdown(self, criteria, data, locator, locator_type="xpath"):
        element = None
        try:
            if locator:
                element = self.get_element(locator, locator_type)
                assert element is not None
                sel = Select(element)

                if criteria == "Index":
                    sel.deselect_by_index(data)
                elif criteria == "Visible Text":
                    sel.deselect_by_visible_text(data)
                elif criteria == "Value":
                    sel.deselect_by_value(data)
        except:
            self.print_log(f"Cannot de-select drop down values based on {criteria} for locator: {locator} - locator_type: {locator_type}")
            print_stack()
            assert element is not None

    # Miscellaneous

    def getFilePath(self, filepath):
        cwd = os.getcwd()
        file = cwd.split("tests")
        fname = file[0] + filepath      #"\\TestData\\EmailDetails.json"
        return fname



