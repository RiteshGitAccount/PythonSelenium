import time

from page_functions.Amazon_ProductPage import Amazon_ProductPage
from utilities.BaseClass import BaseClass


class Amazon_SearchResult(BaseClass):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def select_Product(self):
        self.click_element("//*[text()='Apple iPhone 13 (128GB) - Blue']")
        print("phone clicked")
        time.sleep(10)
        self.switch_to_window(1)
        print("Switched to Window")
        amazon_productpage = Amazon_ProductPage(self.driver)
        return amazon_productpage



