import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def get_chrome_driver():
    """
    This will initialize and return the chromeDrive instance with defined options
    :return:
    """
    options = Options()

    # options.add_argument("--headless") # Run in headless mode
    # Remove "Chrome is being controlled by automated test software" info bar
    options.add_experimental_option("excludeSwitches", ['enable-automation'])

    chromedriver_autoinstaller.install()
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()

    return driver
