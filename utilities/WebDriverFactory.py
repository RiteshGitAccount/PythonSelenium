from selenium import webdriver

from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.service import Service as FirefoxService

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.firefox import GeckoDriverManager


def get_chrome_driver():
    """
    This will initialize and return the chrome driver instance with defined options
    :return:
    """
    options = webdriver.ChromeOptions()
    options.page_load_strategy = 'normal'
    # options.add_argument("--headless")  # Run in headless mode
    options.add_argument("--incognito")  # Run in incognito mode
    # Remove "Chrome is being controlled by automated test software" info bar and some console logs disabled
    options.add_experimental_option("excludeSwitches", ['enable-automation', "enable-logging"])

    driver = webdriver.Chrome(options=options)
    # driver = webdriver.Chrome(options=options,
    #                           service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    return driver


def get_firefox_driver():
    """
    This will initialize and return the firefox driver instance with defined options
    :return:
    """
    options = webdriver.FirefoxOptions()
    options.page_load_strategy = 'normal'
    # options.add_argument("--headless")  # Run in headless mode
    options.add_argument("--private")  # Run in private mode
    driver = webdriver.Firefox(options=options,
                               service=FirefoxService(GeckoDriverManager().install()))
    driver.maximize_window()
    return driver


def get_edge_driver():
    """
    This will initialize and return the edge driver instance with defined options
    :return:
    """
    options = webdriver.EdgeOptions()
    options.page_load_strategy = 'normal'
    # options.add_argument("--headless")  # Run in headless mode
    options.add_argument("--inprivate")  # Run in private mode
    options.add_experimental_option("excludeSwitches", ['enable-automation'])
    driver = webdriver.Edge(options=options,
                            service=EdgeService(EdgeChromiumDriverManager().install()))
    driver.maximize_window()
    return driver


def get_safari_driver():
    """
    This will initialize and return the safari driver instance with defined options
    :return:
    """
    driver = webdriver.Safari()
    driver.maximize_window()
    return driver
