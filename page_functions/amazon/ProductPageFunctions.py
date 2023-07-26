import time

from page_objects.amazon_objects import amazon_productspage_objects
from utilities.BaseClass import BaseClass


class amazon_productpage(BaseClass):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def change_quantity(self):
        self.click_element(amazon_productspage_objects.add_to_cart)
        self.wait_for_element_visibility(amazon_productspage_objects.cart_button)
        self.click_element(amazon_productspage_objects.cart_button)
        time.sleep(10)
        self.wait_for_element_visibility(amazon_productspage_objects.quantity)
        self.select_dropdown_by_value("3", amazon_productspage_objects.quantity)
        # time.sleep(5)
        self.wait_for_element_visibility(amazon_productspage_objects.second_object_recent_history)
        self.click_element(amazon_productspage_objects.second_object_recent_history)
        # time.sleep(5)
        self.wait_for_element_visibility(amazon_productspage_objects.goto_cart)
        self.click_element(amazon_productspage_objects.goto_cart)

    def remove_first_product_from_cart(self):
        self.wait_for_element_visibility(amazon_productspage_objects.first_product_in_cart)
        self.click_element(amazon_productspage_objects.first_product_in_cart)

    def proceed_to_checkout(self):
        self.wait_for_element_visibility(amazon_productspage_objects.proceed_to_checkout)
        self.click_element(amazon_productspage_objects.proceed_to_checkout)
