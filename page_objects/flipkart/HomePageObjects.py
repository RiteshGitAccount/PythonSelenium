class HomePageObjects:
    search_input = "xpath://input[@name='q']"
    username_input = "xpath://span[text()='Enter Email/Mobile number']/parent::label/preceding-sibling::input"
    close_login_window_btn = "xpath://button[text()='✕']"

    product_link = "xpath://div[contains(text(),'{0}')]"
    add_to_cart = "xpath://button[text()='Add to cart']"
    buy_now = "xpath://button[text()='Buy Now']"
