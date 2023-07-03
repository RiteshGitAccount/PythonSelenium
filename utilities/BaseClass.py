import logging
import os.path
import time
from traceback import print_stack

import allure
from allure_commons.types import AttachmentType
from selenium.common.exceptions import *
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.CustomeLogger import custom_logger
from utilities.ExcelReader import read_excel_data, write_excel_data


class BaseClass:
    """
    This class is used for defining generic functions which can be used across the framework
    for better coverage and ease of operations
    """
    log = custom_logger(logging.DEBUG)
    data_excel_file_path = None  # This variable is used for storing the Excel file path
    env_file_path = None  # This variable is used for storing the environment.properties file path
    env_data = None  # This variable is used for storing environment.properties file details in dictionary
    conf_file_path = None  # This variable is used for storing the config.json file path
    conf_data = None  # This variable is used for storing config.json file details in dictionary

    def __init__(self, driver):
        self.driver = driver

    def load_url(self, urls):
        """
        This will load the requested URL on browser
        :param urls:
        :return:
        """
        self.driver.get(urls)

    def read_excel_data(self, sheet_name, col_row):
        """
        This will return the requested Excel cell value from provided sheet name
        :param sheet_name:
        :param col_row:
        :return:
        """
        return read_excel_data(self.data_excel_file_path, sheet_name, col_row)

    def write_excel_data(self, sheet_name, col_row, data):
        """
        This will write the data to the requested Excel cell in provided sheet
        :param sheet_name:
        :param col_row:
        :param data:
        :return:
        """
        return write_excel_data(self.data_excel_file_path, sheet_name, col_row, data)

    def print_log(self, print_statement, log_type="info"):
        """
        This will print the log on console and in log file with provided log type respectively
        :param print_statement:
        :param log_type:
        :return:
        """

        if log_type == "info":
            self.log.info(print_statement)
        elif log_type == "debug":
            self.log.debug(print_statement)
        elif log_type == "error":
            self.log.error(print_statement)
        print(print_statement)

    def screenshots(self, result_message, allure_name="Screenshot"):
        """
        This will take screenshot of web page displayed and attach the same to allure report and
        add it in screenshots folder
        :param result_message:
        :param allure_name:
        :return:
        """
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

    def get_element(self, locator):
        """
        This will return the interactive webDrive element reference for performing different actions on the same
        :param locator:
        :return:
        """
        element = None
        locator = locator.split(":")
        try:
            by_type = self.get_by_type(locator[0])
            element = self.driver.find_element(by_type, locator[1])
        except:
            self.screenshots(f"Element issue", allure_name="Element issue")
            self.print_log(f"Element not fount with locator: '{locator[1]}' and locator_type: '{locator[0]}'",
                           log_type="error")
        assert element is not None
        return element

    def wait_for_element_visibility(self, locator, timeout=10, poll_frequency=1):
        """
        This will wait for requested element to be visible on screen for
        defined time with interval check of 1 sec as default
        :param locator:
        :param timeout:
        :param poll_frequency:
        :return:
        """
        element = None
        locator = locator.split(":")
        try:
            by_type = self.get_by_type(locator[0])
            wait = WebDriverWait(self.driver, timeout=timeout,
                                 poll_frequency=poll_frequency,
                                 ignored_exceptions=[NoSuchElementException, ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.visibility_of_element_located((by_type, locator[1])))
        except:
            self.screenshots(f"Element not visible", allure_name="Element not visible")
            self.print_log(
                f"Element not appeared on the web page with locator: '{locator[1]}' - locator_type: '{locator[0]}' within '{timeout}' seconds",
                log_type="error")
        assert element is not None

    def wait_for_element_invisibility(self, locator, timeout=10, poll_frequency=1):
        """
        This will wait for requested element to be invisible on screen for
        defined time with interval check of 1 sec as default
        :param locator:
        :param timeout:
        :param poll_frequency:
        :return:
        """
        element = None
        locator = locator.split(":")
        try:
            by_type = self.get_by_type(locator[0])
            wait = WebDriverWait(self.driver, timeout=timeout,
                                 poll_frequency=poll_frequency)
            element = wait.until(EC.invisibility_of_element((by_type, locator)))
        except:
            self.screenshots(f"Element is visible", allure_name="Element is visible")
            self.print_log(
                f"Element is still visible on the web page with locator: '{locator[1]}' - locator_type: '{locator[0]}' within '{timeout}' seconds",
                log_type="error")
        assert element is True

    def click_element(self, locator):
        """
        This will click on requested element
        :param locator:
        :return:
        """
        element = None
        try:
            if locator:
                element = self.get_element(locator)
                assert element is not None
                element.click()
        except:
            self.print_log(f"Can not click on the element with locator: '{locator}'")
            print_stack()
            assert element is not None

    def send_text(self, data, locator):
        """
        This will send/set the provided data in the requested text field on screen
        :param data:
        :param locator:
        :return:
        """
        element = None
        try:
            if locator:
                element = self.get_element(locator)
                assert element is not None
                element.clear()
                element.send_keys(data)
        except:
            self.print_log(f"Can not click on the element with locator: '{locator}'")
            print_stack()
            assert element is not None

    # Mouse and Keyboard Actions
    def verify_text(self, data, locator):
        """
        This function is used to verify the text/statement displayed on the screen and verifies if the value is matching.
        If not it will return an error.
        :param data:
        :param locator:
        :return:
        """
        element = None
        try:
            if locator:
                element = self.get_element(locator)
                assert element is not None
                assert element.text == data
        except:
            self.print_log(
                f"Cannot find text / attribute (value) of element with locator: {locator} ")
            print_stack()
            assert element is not None

    def double_click(self, locator):
        """
        This function is used to double-click on a given web element in the screen.
        :param locator:
        :return:
        """
        element = None
        try:
            if locator:
                element = self.get_element(locator)
                assert element is not None
                action = ActionChains(self.driver)
                action.double_click(element).perform()
        except:
            self.print_log(f"Cannot double click on element with locator: {locator}")
            print_stack()
            assert element is not None

    def context_click(self, locator):
        """
        This function is used to right-click on a given web element in the screen.
        :param locator:
        :return:
        """
        element = None
        try:
            if locator:
                element = self.get_element(locator)
                assert element is not None
                action = ActionChains(self.driver)
                action.context_click(element).perform()
        except:
            self.print_log(f"Cannot right click on element with locator: {locator}")
            print_stack()
            assert element is not None

    def move_to_element(self, locator):
        """
        This function is used to move to an element on the screen.
        :param locator:
        :return:
        """
        element = None
        try:
            if locator:
                element = self.get_element(locator)
                assert element is not None
                action = ActionChains(self.driver)
                action.move_to_element(element).perform()
        except:
            self.print_log(f"Cannot move to element with locator: {locator}")
            print_stack()
            assert element is not None

    def move_to_element_with_offset(self, x_offset, y_offset, locator):
        """
        This function is used to shift the mouse pointer(from a web element) as per the offset values provided in the function.
        :param x_offset:
        :param y_offset:
        :param locator:
        :return:
        """
        element = None
        try:
            if locator:
                element = self.get_element(locator)
                assert element is not None
                action = ActionChains(self.driver)
                action.move_to_element_with_offset(element, x_offset, y_offset).perform()
        except:
            self.print_log(
                f"Cannot move to element with offset values :{x_offset} , {y_offset} locator: {locator} ")
            print_stack()
            assert element is not None

    def hover(self, locator):
        """
        This function is used to hover on a given web element.
        :param locator:
        :return:
        """
        element = None
        try:
            if locator:
                element = self.get_element(locator)
                assert element is not None
                action = ActionChains(self.driver)
                action.move_to_element(element).perform()
        except:
            self.print_log(f"Cannot hover on element with locator: {locator}")
            print_stack()
            assert element is not None

    def drag_and_drop(self, source_locator, target_locator):
        """
        This function is used to drag web elements from source location and drop it to the target location.
        :param source_locator:
        :param target_locator:
        :return:
        """
        source_element = None
        target_element = None

        try:
            if source_locator:
                source_element = self.get_element(source_locator)
                target_element = self.get_element(target_locator)
                assert source_element is not None
                assert target_element is not None
                action = ActionChains(self.driver)
                action.drag_and_drop(source_element, target_element).perform()

        except:
            self.print_log(
                f"Cannot drag element from locator: {source_locator} ")
            print_stack()
            assert source_element is not None

    def drag_and_drop_by_offset(self, x_offset, y_offset, locator):
        """
        This function is used drag an element from source location and drop it as per the offset provided in the function.
        :param x_offset:
        :param y_offset:
        :param locator:
        :return:
        """
        element = None
        try:
            if locator:
                element = self.get_element(locator)
                assert element is not None
                action = ActionChains(self.driver)
                action.drag_and_drop_by_offset(element, x_offset, y_offset).perform()
        except:
            self.print_log(f"Cannot drag and drop with offset for locator: {locator} ")
            print_stack()
            assert element is not None

    def drag_and_drop_javascript(self, source, target):  # source & target given as class name in SS - eg: '#coulmn-a'
        """
        This function uses javascript for drag and drop of web elements. This is particularly useful when some webpages
        like HTML5 do not support drag and drop functionality using selenium web driver.
        Note - Need to provide the source and target locators in CSS format for class names eg: '#column-a"
        The javascript file is placed under 'resource' folder, file name is 'drag_and_drop_helper.js'
        :param source:
        :param target:
        :return:
        """
        # cwd = os.getcwd()
        # file = cwd.split("tests")
        # fname = file[0] + "js_scripts\\drag_and_drop_helper.js"

        fname = self.js_script_path + "\\drag_and_drop_helper.js"
        self.print_log(fname)
        with open(fname, 'r') as js_file:
            line = js_file.readline()
            script = ''
            while line:
                script += line
                line = js_file.readline()

        self.driver.execute_script(script + "$('" + source + "').simulateDragDrop({ dropTarget: '" + target + "'});")
        time.sleep(2)

    def horizontal_scroll(self, x_offset, y_offset, locator):
        """
        This function is used to scroll in the horizontal direction - useful when there are text boxes in UI.
        :param x_offset:
        :param y_offset:
        :param locator:
        :return:
        """
        element = None
        try:
            if locator:
                element = self.get_element(locator)
                assert element is not None
                action = ActionChains(self.driver)
                action.click_and_hold(element).move_by_offset(x_offset, y_offset).release().perform()
        except:
            self.print_log(
                f"Cannot scroll horizontally for element with locator: {locator}")
            print_stack()
            assert element is not None

    def is_element_displayed(self, locator):
        """
        This function determines whether a given web element is displayed on the screen.
        It returns value as true or false based on element display.
        :param locator:
        :return:
        """
        element = None
        try:
            if locator:
                element = self.get_element(locator)
                assert element is not None
                return element.is_displayed()
        except:
            self.print_log(f"Element not displayed - locator: {locator}")
            print_stack()
            assert element is not None

    def is_element_selected(self, locator):
        """
        This function determines whether a given web element is selected on the screen.
        It returns value as true or false based on element selection.
        :param locator:
        :return:
        """
        element = None
        try:
            if locator:
                element = self.get_element(locator)
                assert element is not None
                return element.is_selected()
        except:
            self.print_log(f"Element/Check box not selected - locator: {locator}")
            print_stack()
            assert element is not None

    # Browser interactions
    def maximize_browser(self):
        """
        This function is used to maximise the browser window.
        :return:
        """
        self.driver.maximize_window()

    def get_title(self):
        """
        This function returns the title of the web browser
        :return:
        """
        return self.driver.title

    def minimize_browser(self):
        """
        This function is used to minimize the browser window
        :return:
        """
        self.driver.minimize_window()

    def get_url(self):
        """
        This function returns the URL of the web page.
        :return:
        """
        return self.driver.current_url

    def resize_browser(self, x, y):
        """
        This function is used to resize the browser as per the dimensions mentioned in the function.
        :param x:
        :param y:
        :return:
        """

        self.driver.set_window_size(x, y)

    def delete_all_cookies(self):
        """
        This function is used to delete all browser cookies.
        :return:
        """
        self.driver.delete_all_cookies()

    # Iframes
    def switch_to_iframe(self, locator):
        """
        This function  is used to switch to an iframe.
        :param locator:
        :return:
        """
        element = None
        try:
            if locator:
                element = self.get_element(locator)
                assert element is not None
                self.driver.switch_to.frame(element)
        except:
            self.print_log(f"Cannot switch to frame with locator: {locator}")
            print_stack()
            assert element is not None

    def switch_to_default_content(self):
        """
        This function is used to switch back to the webpage from an iframe.
        :return:
        """
        # element = None
        try:
            # if locator:
            # element = self.get_element(locator, locator_type)
            # assert element is not None
            self.driver.switch_to.default_content()
        except:
            self.print_log(f"Cannot switch back to default window from iFrame")
            print_stack()

    # Alerts
    def alert_accept(self):
        """
        This function is used to accept the alert i.e. click on OK/Yes button of the alert.
        :return:
        """
        try:
            alert = self.driver.switch_to.alert
            alert.accept
        except:
            self.print_log(f"Not able to accept alert")
            print_stack()

    def alert_dismiss(self):
        """
        This function is used to dismiss an alert i.e. click on Cancel/No button of the alert.
        :return:
        """
        try:
            alert = self.driver.switch_to.alert
            alert.dismiss
        except:
            self.print_log(f"Not able to dismiss alert")
            print_stack()

    def alert_text(self):
        """
        This function is used to retrieve the text content of the alert and return the same.
        :return:
        """
        try:
            alert = self.driver.switch_to.alert
            text = alert.text
            return text
        except:
            self.print_log(f"Not able retrieve text from the alert")
            print_stack()

    # Window Handles

    def get_current_window_handle(self):
        """
        This function returns the current window handle.
        :return:
        """
        try:
            return self.driver.current_window_handle
        except:
            self.print_log(f"Not able to retrieve current window handle")
            print_stack()

    def get_all_window_handles(self):
        """
        This function returns all the window handles.
        :return:
        """
        try:
            handles = self.driver.window_handles
            return handles
        except:
            self.print_log(f"Not able to retrieve current window handle")
            print_stack()

    def switch_to_window(self, handle_identifier):
        """
        This function is used to switch a different window.
        :param handle_identifier:
        :return:
        """
        try:
            parent_handle = self.get_current_window_handle()
            self.driver.switch_to.window(self.driver.window_handles[handle_identifier])

        except:
            self.print_log(f"Not able to switch to window handle")
            print_stack()

    # Drop downs

    def select_dropdown_by_index(self, data, locator):
        element = None
        try:
            if locator:
                element = self.get_element(locator)
                assert element is not None
                sel = Select(element)
                sel.select_by_index(data)

        except:
            self.print_log(f"Cannot select drop down by index for locator: {locator} ")
            print_stack()
            assert element is not None

    def select_dropdown_by_value(self, data, locator):
        element = None
        try:
            if locator:
                element = self.get_element(locator)
                assert element is not None
                sel = Select(element)
                sel.select_by_value(data)
        except:
            self.print_log(
                f"Cannot select drop down values based on value for locator: {locator}")
            print_stack()
            assert element is not None

    def select_dropdown_by_visible_text(self, data, locator):
        element = None
        try:
            if locator:
                element = self.get_element(locator)
                assert element is not None
                sel = Select(element)
                sel.select_by_visible_text(data)

        except:
            self.print_log(f"Cannot select drop down values based on visible text for locator: {locator}")
            print_stack()
            assert element is not None

    def deselect_dropdown_by_index(self, data, locator):
        element = None
        try:
            if locator:
                element = self.get_element(locator)
                assert element is not None
                sel = Select(element)
                sel.deselect_by_index(data)
        except:
            self.print_log(
                f"Cannot de-select drop down values based on index for locator: {locator}")
            print_stack()
            assert element is not None

    def deselect_dropdown_by_visible_text(self, data, locator):
        element = None
        try:
            if locator:
                element = self.get_element(locator)
                assert element is not None
                sel = Select(element)
                sel.deselect_by_visible_text(data)

        except:
            self.print_log(
                f"Cannot de-select drop down values based on visible text for locator: {locator}")
            print_stack()
            assert element is not None

    def deselect_dropdown_by_value(self, data, locator):
        element = None
        try:
            if locator:
                element = self.get_element(locator)
                assert element is not None
                sel = Select(element)
                sel.deselect_by_value(data)
        except:
            self.print_log(f"Cannot de-select drop down values for locator: {locator}")
            print_stack()
            assert element is not None
