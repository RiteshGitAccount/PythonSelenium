import time

from page_functions.amazon.ProductPageFunctions import ProductPageFunctions
from page_objects.amazon import SearchResultPageObjects
from utilities.BaseClass import BaseClass


class SearchResultPageFunctions(BaseClass):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def select_product(self):
        self.click_element(SearchResultPageObjects.product_name)
        print("phone clicked")
        time.sleep(10)
        self.switch_to_window(1)
        print("Switched to Window")
        amazon_product_page = ProductPageFunctions(self.driver)
        return amazon_product_page
