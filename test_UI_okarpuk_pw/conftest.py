from playwright.sync_api import BrowserContext

import pytest
from test_UI_okarpuk_pw.pages.create_account import CreateAccount
from test_UI_okarpuk_pw.pages.eco_friendly import EcoFriendly
from test_UI_okarpuk_pw.pages.customer_login import CustomerLogin
from test_UI_okarpuk_pw.pages.men_sale import MenSale
from test_UI_okarpuk_pw.pages.sale import Sale
from test_UI_okarpuk_pw.pages.search_result import SearchResult


@pytest.fixture()
def page(context: BrowserContext, playwright):
    playwright.selectors.set_test_id_attribute("id")
    page = context.new_page()
    page.set_viewport_size({'width': 1920, 'height': 1080})
    return page


@pytest.fixture()
def create_account_page(page):
    return CreateAccount(page)


@pytest.fixture()
def eco_friendly_page(page):
    return EcoFriendly(page)


@pytest.fixture()
def customer_login_page(page):
    return CustomerLogin(page)


@pytest.fixture()
def sale_page(page):
    return Sale(page)


@pytest.fixture()
def search_result_page(page):
    return SearchResult(page)


@pytest.fixture()
def men_sale_page(page):
    return MenSale(page)
