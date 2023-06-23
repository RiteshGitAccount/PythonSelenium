import logging
import os
import platform
import pytest
from utilities.CustomeLogger import custom_logger

from utilities.BaseClass import BaseClass
from utilities.DataLoader import load_properties_file_data, load_json_file_data
from utilities.WebDriverFactory import *

ALLUREDIR_OPTION = '--alluredir'
driver = None

log = custom_logger(logging.DEBUG)


def pytest_addoption(parser):
    """
    This is used for getting the command line passed attribute for test execution
    e.g. browser name - on which browser test need to be executed
    :param parser:
    :return:
    """
    parser.addoption("--browser_name", action="store", default="chrome")


@pytest.fixture(scope="session", autouse=True)
def one_time_setup(request):
    """
    This will perform pre-setup action for executing the test cases like:-
    assigning and loading the Excel data, json data, properties data files.
    And post all test execution will add the environment.properties with details required for allure report
    :param request:
    :return:
    """
    BaseClass.data_excel_file_path = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "resources/data.xlsx"))
    BaseClass.env_file_path = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", 'resources/environment.properties'))
    BaseClass.conf_file_path = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", 'resources/conf.json'))

    BaseClass.env_data = load_properties_file_data(BaseClass.env_file_path)
    BaseClass.conf_data = load_json_file_data(BaseClass.conf_file_path)

    yield
    allure_dir = request.config.getoption(ALLUREDIR_OPTION)

    if not allure_dir:
        return
    allure_env_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", allure_dir))
    file_name = allure_env_path + '/environment.properties'
    with open(file_name, "w") as env_file:
        env_file.writelines(f"Browser = {request.config.getoption('browser_name').capitalize()}\n")
        env_file.writelines(f"URL = {BaseClass.env_data.get('url')}\n")
        env_file.writelines(f"User = {platform.node()}\n")
        env_file.writelines(f"System-OS = {platform.system()} - {platform.release()}\n")
        log.info(f"Allure env file created at {file_name}")


@pytest.fixture(scope="function")
def setup(one_time_setup, request):
    """
    This will initialize the driver instances and load the requested url
    And post all test execution, closes all associated windows and ends the WebDriver session gracefully.
    :param one_time_setup:
    :param request:
    :return:
    """
    global driver
    browser_name = request.config.getoption("browser_name")
    log.info(f"{browser_name} browser initialization started")

    match browser_name.lower():
        case "chrome":
            driver = get_chrome_driver()
        case "edge":
            driver = get_edge_driver()
        case "firefox":
            driver = get_firefox_driver()
        case "safari":
            driver = get_safari_driver()
        case _:
            log.info("incorrect browser specified. please check again")

    driver.get(BaseClass.env_data["url"])
    # driver.get(BaseClass.conf_data['sit']['url'])

    if request.cls is not None:
        request.cls.driver = driver

    yield driver

    driver.quit()
