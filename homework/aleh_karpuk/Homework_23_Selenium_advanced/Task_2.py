from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import pytest


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    return chrome_driver


def test_validate_product(driver):
    driver.get('https://magento.softwaretestingboard.com/gear/bags.html')
    driver.execute_script("window.scrollBy(0, 500);")
    bag_element = driver.find_element(By.XPATH, '//ol[@class="products list items product-items"]/li[1]')
    bag_element_text = bag_element.text
    add_to_compare = (driver.find_element
                      (By.XPATH, '//a[@class="action tocompare" and @title="Add to Compare" and @role="button"]'))
    ActionChains(driver).move_to_element(bag_element).move_to_element(add_to_compare).click(add_to_compare).perform()
    driver.execute_script("window.scrollBy(0, 1000);")
    compare_item = driver.find_element(By.XPATH, '//strong[@class="product-item-name"]')
    compare_item_text = compare_item.text
    assert compare_item_text in bag_element_text, "Compare item invalid"
