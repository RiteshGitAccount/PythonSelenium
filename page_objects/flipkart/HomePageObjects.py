class HomePageObjects:
    _search_input = "xpath://input[@name='q']"
    _username_input = "xpath://span[text()='Enter Email/Mobile number']/parent::label/preceding-sibling::input"
    _close_login_window_btn = "xpath://button[text()='✕']"

    _product_link = "xpath://div[contains(text(),'{0}')]"
    _add_to_cart = "xpath://button[text()='Add to cart']"
    _buy_now = "xpath://button[text()='Buy Now']"
