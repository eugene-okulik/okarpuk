from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    return chrome_driver


def test_validate_text(driver):
    driver.get('https://the-internet.herokuapp.com/dynamic_loading/2')
    start_button = driver.find_element(By.XPATH, '//div[@id="start"]/button')
    start_button.click()
    expected_element = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//div[@id="finish"]/h4')))
    expected_text = expected_element.text
    assert expected_text == 'Hello World!'
