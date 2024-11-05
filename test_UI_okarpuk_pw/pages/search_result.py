from playwright.sync_api import Page, Locator, expect

from test_UI_okarpuk_pw.pages.base_page import BasePage
from test_UI_okarpuk_pw.pages.locators import search_result_locators as loc


class SearchResult(BasePage):


    def check_search_no_results_alert_text(self):
        expect(self.find_element(loc.no_results_alert_loc)).to_have_text("Your search returned no results.")
