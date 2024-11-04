from pages.base_page import BasePage
from pages.locators import customer_login_locators as loc


class CustomerLogin(BasePage):


    def check_customer_login_page_name(self):
        customer_login_page_name = self.find_element(loc.customer_login_page_name_loc)
        assert customer_login_page_name.text == "Customer Login",\
            f"The page name - {customer_login_page_name.text} is invalid"


    def check_must_login_alert_text(self):
        must_login_alert = self.find_element(loc.alert_message_loc)
        assert must_login_alert.text == "You must login or register to add items to your wishlist.",\
            f"The alert message text - {must_login_alert.text} is invalid"
