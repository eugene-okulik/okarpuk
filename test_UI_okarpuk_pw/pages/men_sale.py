from playwright.sync_api import expect

from test_UI_okarpuk_pw.pages.base_page import BasePage
from test_UI_okarpuk_pw.pages.locators import men_sale_locators as loc


class MenSale(BasePage):

    def check_men_sale_page_name(self):
        expect(self.find_element(loc.men_sale_page_name_loc)).to_have_text("Men Sale")
