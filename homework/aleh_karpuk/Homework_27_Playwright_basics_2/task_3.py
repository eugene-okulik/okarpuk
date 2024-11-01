from playwright.sync_api import Page, expect


def test_tabs(page: Page):
    page.goto('https://demoqa.com/dynamic-properties')
    color_change_button = page.locator(".mt-4.text-danger.btn.btn-primary")
    color_change_button.wait_for(state="attached")
    expect(color_change_button).to_be_enabled()
    color_change_button.click()
