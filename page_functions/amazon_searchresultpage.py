import time

from page_functions.amazon_productpage import amazon_productpage
from utilities.BaseClass import BaseClass


class amazon_searchresult(BaseClass):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def select_Product(self):
        self.click_element("xpath://*[text()='Apple iPhone 14 (128 GB) - Purple']")
        print("phone clicked")
        time.sleep(10)
        self.switch_to_window(1)
        print("Switched to Window")
        amazon_product_page = amazon_productpage(self.driver)
        return amazon_product_page



