import time

from page_objects.amazon import ProductPageObjects
from utilities.BaseClass import BaseClass


class ProductPageFunctions(BaseClass):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def change_quantity(self):
        self.click_element(ProductPageObjects.add_to_cart)
        self.wait_for_element_visibility(ProductPageObjects.cart_button)
        self.click_element(ProductPageObjects.cart_button)
        time.sleep(10)
        self.wait_for_element_visibility(ProductPageObjects.quantity)
        self.select_dropdown_by_value("3", ProductPageObjects.quantity)
        # time.sleep(5)
        self.wait_for_element_visibility(ProductPageObjects.second_object_recent_history)
        self.click_element(ProductPageObjects.second_object_recent_history)
        # time.sleep(5)
        self.wait_for_element_visibility(ProductPageObjects.goto_cart)
        self.click_element(ProductPageObjects.goto_cart)

    def remove_first_product_from_cart(self):
        self.wait_for_element_visibility(ProductPageObjects.first_product_in_cart)
        self.click_element(ProductPageObjects.first_product_in_cart)

    def proceed_to_checkout(self):
        self.wait_for_element_visibility(ProductPageObjects.proceed_to_checkout)
        self.click_element(ProductPageObjects.proceed_to_checkout)
