from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert

import pytest


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    return chrome_driver


def test_validate_product(driver):
    driver.get('https://www.demoblaze.com/index.html')
    WebDriverWait(driver, 20).until(EC.presence_of_element_located
                                    ((By.XPATH, '//h4[@class="card-title"]/a[@href="prod.html?idp_=4"]')))
    product_button = driver.find_element(By.XPATH, '//h4[@class="card-title"]/a[@href="prod.html?idp_=4"]')
    product_name = product_button.text
    product_button.send_keys(Keys.COMMAND + Keys.RETURN)  # ActionChains не работает с COMMAND и CONTROL на Маке
    tabs = driver.window_handles
    driver.switch_to.window(tabs[1])
    WebDriverWait(driver, 20).until(EC.presence_of_element_located
                                    ((By.XPATH, '//a[@class="btn btn-success btn-lg"]')))
    add_to_cart_button = driver.find_element(By.XPATH, '//a[@class="btn btn-success btn-lg"]')
    add_to_cart_button.click()
    WebDriverWait(driver, 20).until(EC.alert_is_present())
    alert = Alert(driver)
    alert.accept()
    driver.close()
    driver.switch_to.window(tabs[0])
    cart_button = driver.find_element(By.XPATH, '//a[@id="cartur"]')
    cart_button.click()
    WebDriverWait(driver, 20).until(EC.presence_of_element_located
                                    ((By.XPATH, '//tr[@class="success"]/td[2]')))
    product_in_cart = driver.find_element(By.XPATH, '//tr[@class="success"]/td[2]')
    product_in_cart_name = product_in_cart.text
    assert product_name == product_in_cart_name, 'Product name does not match the product name in the shopping cart'
