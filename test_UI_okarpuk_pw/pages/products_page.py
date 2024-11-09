from playwright.sync_api import expect

from test_UI_okarpuk_pw.pages.base_page import BasePage
from test_UI_okarpuk_pw.pages.locators import products_page_locators as loc


class ProductsPage(BasePage):

    def check_products_page_name(self, expected_page_name):
        expect(self.find_element(loc.products_page_name_loc)).to_have_text(expected_page_name)
