from playwright.sync_api import Page, expect, Dialog
from time import sleep


def test_enabled_and_select(page: Page):
    def accept_alert(alert: Dialog):
        alert.accept()
    page.on('dialog', accept_alert)
    page.goto('https://www.qa-practice.com/elements/alert/confirm')
    page.locator('.a-button').click()
    result_locator = page.locator('#result-text')
    expect(result_locator).to_have_text('Ok')
