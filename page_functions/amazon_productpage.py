import time

from utilities.BaseClass import BaseClass


class amazon_productpage(BaseClass):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def change_quantity(self):
        self.click_element("id:add-to-cart-button")
        self.wait_for_element_visibility("xpath://*[@id='attach-sidesheet-view-cart-button']/span/input")
        self.click_element("xpath://*[@id='attach-sidesheet-view-cart-button']/span/input")
        time.sleep(10)
        self.wait_for_element_visibility("xpath://select[@name='quantity']")
        self.select_dropdown_by_value("3", "xpath://select[@name='quantity']")
        # time.sleep(5)
        self.wait_for_element_visibility("xpath://*[@id='a-autoid-9']/span/input")
        self.click_element("xpath://*[@id='a-autoid-9']/span/input")
        # time.sleep(5)
        self.wait_for_element_visibility("xpath://*[@id='sw-gtc']/span/a")
        self.click_element("xpath://*[@id='sw-gtc']/span/a")
    def remove_first_product_from_cart(self):
        self.wait_for_element_visibility("xpath://div[@data-name='Active Items']/div[3]/div[4]/div/div[2]/div[1]/span[2]/span/input")
        self.click_element("xpath://div[@data-name='Active Items']/div[3]/div[4]/div/div[2]/div[1]/span[2]/span/input")
    def proceed_to_checkout(self):
        self.wait_for_element_visibility("xpath://*[@value='Proceed to checkout']")
        self.click_element("xpath://*[@value='Proceed to checkout']")
