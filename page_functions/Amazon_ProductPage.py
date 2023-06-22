import time

from utilities.BaseClass import BaseClass


class Amazon_ProductPage(BaseClass):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def change_quantity(self):
        self.click_element("add-to-cart-button", locator_type="id")
        #time.sleep(10)
        self.wait_for_element_visibility("//*[@id='attach-sidesheet-view-cart-button']/span/input")
        self.click_element("//*[@id='attach-sidesheet-view-cart-button']/span/input")
        #time.sleep(10)
        self.wait_for_element_visibility("//select[@name='quantity']", locator_type="xpath")
        self.select_dropdown_by_value("3", "//select[@name='quantity']", locator_type="xpath")
        #time.sleep(5)
        self.wait_for_element_visibility("//*[@id='a-autoid-9']/span/input")
        self.click_element("//*[@id='a-autoid-9']/span/input")
        #time.sleep(5)
        self.wait_for_element_visibility("//*[@id='sw-gtc']/span/a")
        self.click_element("//*[@id='sw-gtc']/span/a")

    def remove_first_product_from_cart(self):
        self.wait_for_element_visibility("//div[@data-name='Active Items']/div[3]/div[4]/div/div[2]/div[1]/span[2]/span/input")
        self.click_element("//div[@data-name='Active Items']/div[3]/div[4]/div/div[2]/div[1]/span[2]/span/input")

    def proceed_to_checkout(self):
        self.wait_for_element_visibility("//*[@value='Proceed to checkout']")
        self.click_element("//*[@value='Proceed to checkout']")
