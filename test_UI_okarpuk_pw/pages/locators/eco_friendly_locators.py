from selenium.webdriver.common.by import By


products_list_loc = (By.XPATH, '//li[@class="item product product-item"]')
price_button_loc = (By.XPATH, '//div[normalize-space()="Price"]')
price_range_40_50_loc = (By.XPATH, '//span[normalize-space()="$49.99"]')
choose_size_button_loc = (By.XPATH, '//div[@aria-label="Size"]/div[@index="0"]')
choose_color_button_loc = (By.XPATH, '//div[@aria-label="Color"]/div[@index="1"]')
add_to_cart_button_loc = (By.XPATH, '//button[@title="Add to Cart"]')
cart_button_loc = (By.XPATH, '//a[@class="action showcart"]')
product_name_in_cart_loc = (By.XPATH, '//strong[@class="product-item-name"]')
product_price_in_cart_loc = (By.XPATH, '//div[@class="price-container"]')
