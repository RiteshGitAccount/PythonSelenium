import time

from page_functions.amazon_searchresultpage import amazon_searchresult
from page_objects.FunctionalPageObjects import FunctionalPageObjects
from utilities.BaseClass import BaseClass


class amazon_homepage(BaseClass):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def homepage_search(self, search_text):
        self.click_element(FunctionalPageObjects.homepage_searchbox)
        self.send_text("iphone", FunctionalPageObjects.homepage_searchbox)
        self.click_element(FunctionalPageObjects.homepage_findbutton)
        time.sleep(5)
        amazon_search_result = amazon_searchresult(self.driver)
        return amazon_search_result
