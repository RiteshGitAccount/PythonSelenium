import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class WebDriverFactory:

    def get_chrome_driver(self):
        options = Options()
        # options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        chromedriver_autoinstaller.install()
        driver = webdriver.Chrome(options=options)
        driver.maximize_window()

        return driver
