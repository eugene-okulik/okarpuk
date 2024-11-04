import pytest


@pytest.mark.smoke
def test_check_empty_cart_message(sale_page):
    sale_page.open_page()
    sale_page.click_on_cart_icon()
    sale_page.check_empty_cart_message("You have no items in your shopping cart.")


@pytest.mark.smoke
def test_search_invalid_product(sale_page, search_result_page):
    product_name = "!@#12345"
    sale_page.open_page()
    sale_page.find_product_by_search(product_name)
    search_result_page.check_search_no_results_alert_text()


@pytest.mark.smoke
def test_mens_bargains_banner(sale_page, men_sale_page):
    sale_page.open_page()
    sale_page.click_on_mens_bargains_banner()
    men_sale_page.check_men_sale_page_name()
