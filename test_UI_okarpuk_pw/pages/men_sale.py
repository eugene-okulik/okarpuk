from pages.base_page import BasePage
from pages.locators import men_sale_locators as loc


class MenSale(BasePage):


    def check_men_sale_page_name(self):
        men_sale_page_name = self.find_element(loc.men_sale_page_name_loc)
        assert men_sale_page_name.text == "Men Sale", f"The page name - {men_sale_page_name.text} is invalid"
