from time import sleep

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

from test_UI_okarpuk_pw.pages.base_page import BasePage
from test_UI_okarpuk_pw.pages.locators import eco_friendly_locators as loc


class EcoFriendly(BasePage):
    page_url = '/collections/eco-friendly.html'
    product_name_text = None
    product_price_text = None


    def get_one_of_products(self, product_index):
        products_list = self.find_all_elements(loc.products_list_loc)
        return products_list[product_index]

    def add_product_to_wish_list(self, selected_product):
        self.driver.execute_script("window.scrollBy(0, 400);")
        add_to_wish_list_button = (selected_product.find_element
                                   (By.XPATH,'.//a[@class="action towishlist" '
                                             'and @title="Add to Wish List" and @role="button"]')
                                   )
        (ActionChains(self.driver).
         move_to_element(selected_product).
         move_to_element(add_to_wish_list_button).
         click().perform()
         )

    def check_products_by_40_50_price_range(self):
        self.driver.execute_script("window.scrollBy(0, 2000);")
        price_button = self.find_element(loc.price_button_loc)
        price_range_40_50 = self.find_element(loc.price_range_40_50_loc)
        price_button.click()
        price_range_40_50.click()
        products_list = self.find_all_elements(loc.products_list_loc)
        for product in products_list:
            price_element = product.find_element(By.XPATH, './/span[@class="price"]')
            price_text = price_element.text
            price_float = float(price_text.replace('$', '').strip())
            assert 40.00 <= price_float <= 49.99, f"Price {price_float} not in range"

    def add_product_to_cart(self, selected_product):
        self.driver.execute_script("window.scrollBy(0, 600);")
        product_name = selected_product.find_element(By.XPATH, '//a[@class="product-item-link"]')
        product_price = selected_product.find_element(By.XPATH, '//span[@class="price"]')
        choose_size_button =self.find_element(loc.choose_size_button_loc)
        choose_color_button =self.find_element(loc.choose_color_button_loc)
        add_to_cart_button = self.find_element(loc.add_to_cart_button_loc)
        self.product_name_text = product_name.text
        self.product_price_text = product_price.text
        (ActionChains(self.driver).
         move_to_element(selected_product).
         move_to_element(choose_size_button).click(choose_size_button).
         move_to_element(choose_color_button).click(choose_color_button).
         move_to_element(add_to_cart_button).click(add_to_cart_button).
         perform()
         )
        self.driver.execute_script("window.scrollBy(0, -600);")
        sleep(3)  # по-другому никак не получается

    def open_cart(self):
        cart_button = self.find_element(loc.cart_button_loc)
        cart_button.click()

    def check_product_name_in_cart(self):
        product_name_in_cart = self.find_element(loc.product_name_in_cart_loc)
        product_name_in_cart_text = product_name_in_cart.text
        assert self.product_name_text == product_name_in_cart_text, "The product name do not match"

    def check_product_price_in_cart(self):
        product_price_in_cart = self.find_element(loc.product_price_in_cart_loc)
        product_price_in_cart_text = product_price_in_cart.text
        assert self.product_price_text == product_price_in_cart_text, "The product price do not match"
