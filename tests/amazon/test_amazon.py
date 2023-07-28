import time
import unittest

import allure
import pytest

from page_functions.amazon.HomePageFunctions import HomePageFunctions
from utilities.BaseClass import BaseClass


@pytest.mark.usefixtures("setup")
@allure.epic("Amazon")
@allure.feature("Feature_1")
@allure.story("Story_1")
@allure.tag("tag 1")
@allure.description("desc 1")
@allure.severity(allure.severity_level.NORMAL)
class AmazonTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, setup):
        self.amazon = HomePageFunctions(self.driver)
        self.base = BaseClass(self.driver)

    @allure.title("Amazon demo")
    @allure.tag("Amazon Demo")
    @allure.description("To demo amazon workflow using python automation framework")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_end_to_end_amazon_workflow(self):
        self.base.load_url(self.base.env_data["url2"])

        search_result = self.amazon.homepage_search("iphone")

        product_page = search_result.select_product()
        product_page.change_quantity()
        product_page.remove_first_product_from_cart()
        product_page.proceed_to_checkout()
        time.sleep(10)

