import time
import unittest

import allure
import pytest

from page_functions.flipkart.HomePageFunctions import HomePageFunctions
from utilities.BaseClass import BaseClass

@allure.epic("Flipkart")
@pytest.mark.usefixtures("setup")
class FlipkartTest(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def classSetup(self, setup):
        self.fun = HomePageFunctions(self.driver)
        self.base = BaseClass(self.driver)

    @allure.title("Flipkart demo")
    @allure.tag("Flipkart demo")
    @allure.description("To demo amazon workflow using python automation framework")
    def test_add_to_cart(self):
        self.base.load_url(self.base.env_data["url3"])

        product = self.base.read_excel_data("A1")
        self.fun.enter_login_username(login_user_detail=9191919191)
        time.sleep(2)
        self.fun.close_login_window()
        time.sleep(2)
        self.fun.search_product(product)
        time.sleep(2)
        self.fun.select_product(product)
        time.sleep(2)
        self.base.switch_to_window(1)
        time.sleep(2)
        self.fun.add_to_cart()
        time.sleep(2)
        self.base.close_current_tab()
        time.sleep(2)
        self.base.switch_to_window(0)
        time.sleep(2)
        self.fun.search_product("mobile")
        time.sleep(2)
