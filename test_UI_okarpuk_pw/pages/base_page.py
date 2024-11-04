from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    base_url = 'https://magento.softwaretestingboard.com'
    page_url = None


    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open_page(self):
        if self.page_url:
            self.driver.get(f'{self.base_url}{self.page_url}')
        else:
            raise NotImplementedError('Page can not be opened for this page class')

    def find_element(self, locator: tuple):
        return self.driver.find_element(*locator)

    def find_all_elements(self, locator: tuple):
        return self.driver.find_elements(*locator)

    def check_current_url(self, expected_url):
        current_page_url = self.driver.current_url
        assert current_page_url == expected_url, f"Expected URL: {expected_url}, but got: {current_page_url}"
