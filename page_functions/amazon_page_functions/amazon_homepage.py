import time

from page_functions.amazon_page_functions.amazon_searchresultpage import amazon_searchresult
from page_objects.amazon_objects import amazon_homepage_objects
from utilities.BaseClass import BaseClass


class amazon_homepage(BaseClass):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def homepage_search(self, search_text):
        self.click_element(amazon_homepage_objects.homepage_searchbox)
        self.send_text("iphone", amazon_homepage_objects.homepage_searchbox)
        self.click_element(amazon_homepage_objects.homepage_findbutton)
        time.sleep(5)
        amazon_search_result = amazon_searchresult(self.driver)
        return amazon_search_result
