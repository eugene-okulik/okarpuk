from test_UI_okarpuk_pw.pages.base_page import BasePage
from test_UI_okarpuk_pw.pages.locators import search_result_locators as loc


class SearchResult(BasePage):


    def check_search_no_results_alert_text(self):
        no_results_alert = self.find_element(loc.no_results_alert_loc)
        assert no_results_alert.text == "Your search returned no results.",\
            f"The alert message text - {no_results_alert.text} is invalid"
