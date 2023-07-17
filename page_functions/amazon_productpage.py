import time

from page_objects.FunctionalPageObjects import FunctionalPageObjects
from utilities.BaseClass import BaseClass


class amazon_productpage(BaseClass):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def change_quantity(self):
        self.click_element(FunctionalPageObjects.add_to_cart)
        self.wait_for_element_visibility(FunctionalPageObjects.cart_button)
        self.click_element(FunctionalPageObjects.cart_button)
        time.sleep(10)
        self.wait_for_element_visibility(FunctionalPageObjects.quantity)
        self.select_dropdown_by_value("3", FunctionalPageObjects.quantity)
        # time.sleep(5)
        self.wait_for_element_visibility(FunctionalPageObjects.second_object_recent_history)
        self.click_element(FunctionalPageObjects.second_object_recent_history)
        # time.sleep(5)
        self.wait_for_element_visibility(FunctionalPageObjects.goto_cart)
        self.click_element(FunctionalPageObjects.goto_cart)

    def remove_first_product_from_cart(self):
        self.wait_for_element_visibility(FunctionalPageObjects.first_product_in_cart)
        self.click_element(FunctionalPageObjects.first_product_in_cart)

    def proceed_to_checkout(self):
        self.wait_for_element_visibility(FunctionalPageObjects.proceed_to_checkout)
        self.click_element(FunctionalPageObjects.proceed_to_checkout)
