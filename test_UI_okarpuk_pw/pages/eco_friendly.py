from playwright.sync_api import expect

from test_UI_okarpuk_pw.pages.base_page import BasePage
from test_UI_okarpuk_pw.pages.locators import eco_friendly_locators as loc


class EcoFriendly(BasePage):
    page_url = '/collections/eco-friendly.html'
    product_name_text = None
    product_price_text = None

    def get_one_of_products(self, product_index):
        selected_product = self.page.locator(loc.products_list_loc).nth(product_index)
        return selected_product

    def add_product_to_wish_list(self, selected_product):
        self.page.evaluate("window.scrollBy(0, 400);")
        add_to_wish_list_button = (selected_product.locator(
            'a.action.towishlist[title="Add to Wish List"][role="button"]')
        )
        selected_product.hover()
        add_to_wish_list_button.click()

    def check_products_by_40_50_price_range(self):
        price_button = self.find_element(loc.price_button_loc)
        price_range_40_50 = self.find_element(loc.price_range_40_50_loc)
        price_button.click()
        price_range_40_50.click()
        products_list = self.page.locator(loc.products_list_loc).all()
        for product in products_list:
            price_element = product.locator('span.price')
            price_text = price_element.inner_text()
            price_float = float(price_text.replace('$', '').strip())
            assert 40.00 <= price_float <= 49.99
            # expect не может сравнить float значения, поэтому использую assert

    def add_product_to_cart(self, selected_product):
        product_name = selected_product.locator('a.product-item-link')
        product_price = selected_product.locator('span.price')
        choose_size_button = selected_product.locator(loc.choose_size_button_loc)
        choose_color_button = selected_product.locator(loc.choose_color_button_loc)
        add_to_cart_button = selected_product.locator(loc.add_to_cart_button_loc)
        self.product_name_text = product_name.inner_text()
        self.product_price_text = product_price.inner_text()
        selected_product.hover()
        choose_size_button.click()
        choose_color_button.click()
        add_to_cart_button.click()

    def open_cart(self):
        cart_button = self.find_element(loc.cart_button_loc)
        cart_button.click()

    def check_product_name_in_cart(self):
        product_name_in_cart = self.page.locator(loc.product_name_in_cart_loc)
        expect(product_name_in_cart).to_have_text(self.product_name_text)

    def check_product_price_in_cart(self):
        product_price_in_cart = self.page.locator(loc.product_price_in_cart_loc)
        expect(product_price_in_cart).to_have_text(self.product_price_text)
