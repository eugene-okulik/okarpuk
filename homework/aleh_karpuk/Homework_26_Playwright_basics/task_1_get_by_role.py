from playwright.sync_api import Page, expect


def test_get_by_role(page: Page):
    page.goto('https://the-internet.herokuapp.com/')
    page.get_by_role('link', name='Form Authentication').click()
    username_field = page.get_by_role('textbox', name='username')
    username_field.fill('tomsmith')
    password_field = page.get_by_role('textbox', name='password')
    password_field.fill('SuperSecretPassword!')
    page.get_by_role('button', name='Login').click()
