from playwright.sync_api import expect

from test_UI_okarpuk_pw.pages.base_page import BasePage
from test_UI_okarpuk_pw.pages.locators import customer_login_locators as loc


class CustomerLogin(BasePage):

    def check_customer_login_page_name(self, expected_page_name):
        expect(self.find_element(loc.customer_login_page_name_loc)).to_have_text(expected_page_name)

    def check_must_login_alert_text(self, expected_text):
        alert_message = self.page.locator(loc.alert_message_loc).first
        expect(alert_message).to_have_text(expected_text)
