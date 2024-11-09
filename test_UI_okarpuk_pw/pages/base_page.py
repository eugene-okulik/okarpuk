from playwright.sync_api import Page, Locator
import allure


class BasePage:
    base_url = 'https://magento.softwaretestingboard.com'
    page_url = None

    def __init__(self, page: Page):
        self.page = page

    @allure.step('Open the page')
    def open_page(self):
        if self.page_url:
            self.page.goto(f'{self.base_url}{self.page_url}')
        else:
            raise NotImplementedError('Page can not be opened for this page class')

    @allure.step('Find element by locator')
    def find_element(self, locator) -> Locator:
        return self.page.locator(locator)

    @allure.step('Check current page URL')
    def check_current_url(self, expected_url):
        current_page_url = self.page.url
        assert current_page_url == expected_url, f"Expected URL: {expected_url}, but got: {current_page_url}"
