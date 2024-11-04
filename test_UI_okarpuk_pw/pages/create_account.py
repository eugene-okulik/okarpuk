from pages.base_page import BasePage
from pages.locators import create_account_locators as loc


class CreateAccount(BasePage):
    page_url = '/customer/account/create/'


    def fill_create_account_form(self, first_name, last_name, email, password, confirm_password):
        first_name_field = self.find_element(loc.first_name_field_loc)
        last_name_field = self.find_element(loc.last_name_field_loc)
        email_field = self.find_element(loc.email_field_loc)
        password_field = self.find_element(loc.password_field_loc)
        confirm_password_field = self.find_element(loc.confirm_password_field_loc)
        create_account_button = self.find_element(loc.create_account_button_loc)
        first_name_field.send_keys(first_name)
        last_name_field.send_keys(last_name)
        email_field.send_keys(email)
        password_field.send_keys(password)
        confirm_password_field.send_keys(confirm_password)
        self.driver.execute_script("window.scrollBy(0, 2000);")
        create_account_button.click()

    def check_empty_last_name_error(self, expected_error_text):
        last_name_error = self.find_element(loc.last_name_empty_error_loc)
        assert last_name_error.text == expected_error_text, \
            f"Expected error text: {expected_error_text}, but got: {last_name_error.text}"

    def check_js_injection_error(self, expected_error_text):
        js_injection_error = self.find_element(loc.js_injection_error_loc)
        assert js_injection_error.text == expected_error_text, "JS injection can't be entered"
