import pytest


@pytest.mark.smoke
def test_add_product_to_wish_list_without_login(eco_friendly_page, customer_login_page):
    eco_friendly_page.open_page()
    selected_product = eco_friendly_page.get_one_of_products(0)
    eco_friendly_page.add_product_to_wish_list(selected_product)
    customer_login_page.check_customer_login_page_name()
    customer_login_page.check_must_login_alert_text("You must login or register to add items to your wishlist.")


@pytest.mark.smoke
def test_40_50_price_filter(eco_friendly_page, customer_login_page):
    eco_friendly_page.open_page()
    eco_friendly_page.check_products_by_40_50_price_range()


@pytest.mark.smoke
def test_add_product_to_cart_and_check_name_and_price(eco_friendly_page):
    eco_friendly_page.open_page()
    selected_product = eco_friendly_page.get_one_of_products(0)
    eco_friendly_page.add_product_to_cart(selected_product)
    eco_friendly_page.open_cart()
    eco_friendly_page.check_product_name_in_cart()
    eco_friendly_page.check_product_price_in_cart()
