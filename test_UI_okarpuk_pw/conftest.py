import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from pages.create_account import CreateAccount
from pages.eco_friendly import EcoFriendly
from pages.customer_login import CustomerLogin
from pages.men_sale import MenSale
from pages.sale import Sale
from pages.search_result import SearchResult


@pytest.fixture()
def driver():
    options = Options()
    # options.add_argument("--headless")
    chrome_driver = webdriver.Chrome(options=options)
    chrome_driver.maximize_window()
    return chrome_driver

@pytest.fixture()
def create_account_page(driver):
    return CreateAccount(driver)

@pytest.fixture()
def eco_friendly_page(driver):
    return EcoFriendly(driver)

@pytest.fixture()
def customer_login_page(driver):
    return CustomerLogin(driver)

@pytest.fixture()
def sale_page(driver):
    return Sale(driver)

@pytest.fixture()
def search_result_page(driver):
    return SearchResult(driver)

@pytest.fixture()
def men_sale_page(driver):
    return MenSale(driver)
