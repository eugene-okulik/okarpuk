from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import pytest
from  time import sleep


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    return chrome_driver


def test_validate_text(driver):
    driver.get('https://www.qa-practice.com/elements/select/single_select')

    select_language_field = driver.find_element(By.XPATH, '//select[@name="choose_language"]')
    submit_button = driver.find_element(By.XPATH, '//input[@name="submit"]')

    dropdown = Select(select_language_field)
    dropdown.select_by_value('5')
    selected_option_text = dropdown.first_selected_option.text
    submit_button.click()

    output_result = driver.find_element(By.XPATH, '//p[@id="result-text"]')
    output_text = output_result.text

    assert selected_option_text == output_text, f'Text invalid. Expected {selected_option_text}, but got {output_text}'

sleep(5)
