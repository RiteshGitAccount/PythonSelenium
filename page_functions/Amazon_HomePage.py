import time

from page_functions.Amazon_SearchResult import Amazon_SearchResult
from utilities.BaseClass import BaseClass


class Amazon_HomePage(BaseClass):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def homepage_search(self, search_text):
        self.click_element("//input[@id='twotabsearchtextbox']", locator_type="xpath")
        self.send_text("iphone", "//input[@id='twotabsearchtextbox']", locator_type="xpath")
        self.click_element("//input[@id='nav-search-submit-button']")
        time.sleep(5)
        amazon_searchresult = Amazon_SearchResult(self.driver)
        return amazon_searchresult

