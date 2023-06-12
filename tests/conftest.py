import os
import platform
import pytest
from selenium import webdriver

from utilities.BaseClass import BaseClass
from utilities.DataLoader import load_properties_file_data, load_json_file_data
from utilities.WebDriverFactory import get_chrome_driver

ALLUREDIR_OPTION = '--alluredir'
driver = None


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome")


@pytest.fixture(scope="session", autouse=True)
def one_time_setup(request):
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

    with open(allure_env_path + '/environment.properties', "w") as env_file:
        env_file.writelines(f"Browser = {request.config.getoption('browser_name').capitalize()}\n")
        env_file.writelines(f"URL = {BaseClass.env_data.get('url')}\n")
        env_file.writelines(f"User = {platform.node()}\n")
        env_file.writelines(f"System-OS = {platform.system()} - {platform.release()}\n")


@pytest.fixture(scope="function")
def setup(one_time_setup, request):
    global driver
    browser_name = request.config.getoption("browser_name")

    if browser_name == "chrome":
        driver = get_chrome_driver()
    elif browser_name == "firefox":
        # driver = webdriver.Firefox(executable_path="D:\\FirefoxDriver\\geckodriver.exe")
        driver = webdriver.Firefox()
    elif browser_name == "IE":
        print("IE driver")

    driver.get(BaseClass.env_data["url"])
    # driver.get(BaseClass.conf_data['sit']['url'])

    if request.cls is not None:
        request.cls.driver = driver

    yield driver

    driver.close()
