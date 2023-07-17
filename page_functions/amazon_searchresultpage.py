import time

from page_functions.amazon_productpage import amazon_productpage
from page_objects.FunctionalPageObjects import FunctionalPageObjects
from utilities.BaseClass import BaseClass


class amazon_searchresult(BaseClass):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def select_Product(self):
        self.click_element(FunctionalPageObjects.product_name)
        print("phone clicked")
        time.sleep(10)
        self.switch_to_window(1)
        print("Switched to Window")
        amazon_product_page = amazon_productpage(self.driver)
        return amazon_product_page



