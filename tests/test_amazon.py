import time
import unittest

import allure
import pytest

from page_functions.amazon_page_functions.amazon_homepage import amazon_homepage
from utilities.BaseClass import BaseClass


@pytest.mark.usefixtures("setup")
@allure.epic("Epic_1")
@allure.feature("Feature_1")
@allure.story("Story_1")
@allure.tag("tag 1")
@allure.description("desc 1")
@allure.severity(allure.severity_level.NORMAL)
class test_amazon(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, setup):
        self.amazon = amazon_homepage(self.driver)
        self.base = BaseClass(self.driver)

    @allure.title("Check severity level - CRITICAL")
    @allure.tag("Amazon Demo")
    @allure.description("To demo amazon workflow using python automation framework")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_end_to_end_amazon_workflow(self):
        self.base.load_url(self.base.env_data["url2"])
        Amazon_SearchResult = self.amazon.homepage_search("iphone")

        Amazon_ProductPage = Amazon_SearchResult.select_Product()
        Amazon_ProductPage.change_quantity()
        Amazon_ProductPage.remove_first_product_from_cart()
        Amazon_ProductPage.proceed_to_checkout()
        time.sleep(10)

