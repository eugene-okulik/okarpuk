from playwright.sync_api import expect

from test_UI_okarpuk_pw.pages.base_page import BasePage
from test_UI_okarpuk_pw.pages.locators import create_account_locators as loc


class CreateAccount(BasePage):
    page_url = '/customer/account/create/'


    def fill_create_account_form(self, first_name, last_name, email, password, confirm_password):
        first_name_field = self.find_element(loc.first_name_field_loc)
        last_name_field = self.find_element(loc.last_name_field_loc)
        email_field = self.find_element(loc.email_field_loc)
        password_field = self.find_element(loc.password_field_loc)
        confirm_password_field = self.find_element(loc.confirm_password_field_loc)
        create_account_button = self.find_element(loc.create_account_button_loc)
        first_name_field.fill(first_name)
        last_name_field.fill(last_name)
        email_field.fill(email)
        password_field.fill(password)
        confirm_password_field.fill(confirm_password)
        create_account_button.click()

    def check_empty_last_name_error(self, expected_error_text):
        expect(self.find_element(loc.last_name_empty_error_loc)).to_have_text(expected_error_text)

    def check_js_injection_error(self, expected_error_text):
        expect(self.find_element(loc.js_injection_error_loc)).to_have_text(expected_error_text)
