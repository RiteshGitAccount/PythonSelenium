import time

from page_functions.amazon.SearchResultPageFunctions import SearchResultPageFunctions
from page_objects.amazon import HomePageObjects
from utilities.BaseClass import BaseClass


class HomePageFunctions(BaseClass):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def homepage_search(self, search_text):
        self.click_element(HomePageObjects.homepage_search_box)
        self.send_text(HomePageObjects.homepage_search_box, search_text)
        self.click_element(HomePageObjects.homepage_find_button)
        time.sleep(5)
        amazon_search_result = SearchResultPageFunctions(self.driver)
        return amazon_search_result
