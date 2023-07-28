from page_objects.flipkart.HomePageObjects import HomePageObjects
from utilities.BaseClass import BaseClass


class HomePageFunctions(BaseClass):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.hm_obj = HomePageObjects()

    def search_product(self, product):
        self.send_text(self.hm_obj.search_input, product)
        self.hit_enter()
        self.print_log(f"{product=} searched")

    def enter_login_username(self, login_user_detail):
        assert login_user_detail != "", "Login detail can not be blank/empty"
        assert login_user_detail is not None, "Login detail can not be blank/empty"
        if self.wait_for_element_visibility(self.hm_obj.close_login_window_btn):
            if login_user_detail != "":
                self.send_text(self.hm_obj.username_input, login_user_detail)
                self.print_log(f"User email or mobile provide for login is: {login_user_detail}")

        self.print_log(f"User email or mobile not provide for login or skipped: {login_user_detail}")

    def close_login_window(self):
        if self.wait_for_element_visibility(self.hm_obj.close_login_window_btn):
            self.click_element(self.hm_obj.close_login_window_btn)
            self.print_log("Login window closed")
        self.wait_for_element_invisibility(self.hm_obj.close_login_window_btn)

    def select_product(self, product):
        self.click_element(self.hm_obj.product_link.format(product))
        self.print_log(f"{product=} selected")

    def add_to_cart(self):
        self.click_element(self.hm_obj.add_to_cart)
        self.print_log("Add to cart button clicked")
