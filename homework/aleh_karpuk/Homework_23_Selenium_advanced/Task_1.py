from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
import pytest
from time import sleep


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    chrome_driver.implicitly_wait(5)
    return chrome_driver


def test_validate_product(driver):

    driver.get('https://www.demoblaze.com/index.html')


    product_button = driver.find_element(By.CSS_SELECTOR, 'h4.card-title > a.hrefch[href="prod.html?idp_=4"]')
    product_button.send_keys(Keys.COMMAND + Keys.RETURN) # ActionChains не работает с COMMAND и CONTROL на Маке
    tabs = driver.window_handles
    driver.switch_to.window(tabs[1])

    add_to_cart_button = driver.find_element(By.XPATH, '//a[@class="btn btn-success btn-lg"]')
    add_to_cart_button.click()

    WebDriverWait(driver, 20).until(EC.alert_is_present()) # Без ожидания тест падает
    alert = Alert(driver)
    alert.accept()

    driver.close()
    driver.switch_to.window(tabs[0])

    cart_button = driver.find_element(By.XPATH, '//a[@id="cartur"]')
    cart_button.click()

    sleep(5)

    #
    #
    #
    # expected_element = WebDriverWait(driver, 20).until(EC.visibility_of_element_located
    #                                                    ((By.XPATH, '//div[@id="finish"]/h4')))
    #
    #
    #
    # expected_text = expected_element.text
    #
    #
    #
    #
    # assert expected_text == 'Hello World!'


