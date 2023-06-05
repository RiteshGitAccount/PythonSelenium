import platform
import shutil
from pathlib import Path
import pytest
from selenium import webdriver
from utilities.WebDriverFactory import WebDriverFactory

driver = None

ALLURE_ENVIRONMENT_PROPERTIES_FILE = 'environment.properties'
ALLUREDIR_OPTION = '--alluredir'
browser_name = None
# URL = "https://www.flipkart.com/"
URL = "http://the-internet.herokuapp.com/"


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome")


@pytest.fixture(scope="class")
def setup(request):
    global driver
    global browser_name
    browser_name = request.config.getoption("browser_name")
    wdf = WebDriverFactory()
    if browser_name == "chrome":
        driver = wdf.get_chrome_driver()
    elif browser_name == "firefox":
        # driver = webdriver.Firefox(executable_path="D:\\FirefoxDriver\\geckodriver.exe")
        driver = webdriver.Firefox()
    elif browser_name == "IE":
        print("IE driver")
    driver.get(URL)
    driver.maximize_window()

    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    driver.close()


@pytest.fixture(scope="session", autouse=True)
def allure_env(request):
    yield
    alluredir = request.config.getoption(ALLUREDIR_OPTION)

    if not alluredir:
        return
    cwd = Path.cwd()
    print(cwd)
    # env_path = os.path.join(cwd, os.path.sep + "resources" + os.path.sep + "environment.properties")
    # allure_env_path = os.path.join(cwd, alluredir)
    # shutil.copy(env_path, allure_env_path)
    shutil.copyfile("../resources/environment.properties", "../a_report/environment.properties")

    with open("../a_report/environment.properties", "a") as env_file:
        # Writing data to a file
        env_file.writelines(f"User = {platform.node()}\n")
        env_file.writelines(f"System-OS = {platform.system()} - {platform.release()}\n")
