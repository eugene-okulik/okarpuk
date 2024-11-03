from playwright.sync_api import Page, expect, Request, Route, APIResponse
import re
import json


def test_iphone_title_interception(page: Page):
    def modify_product_name(route: Route):
        response = route.fetch()
        body = response.json()
        body['body']['digitalMat'][0]['familyTypes'][0]['productName'] = 'яблокофон 16 про'
        body = json.dumps(body)
        route.fulfill(
            response=response,
            body=body)
    page.route(re.compile('digitalmat$'), modify_product_name)
    page.goto('https://www.apple.com/shop/buy-iphone')
    page.get_by_role('button', name='Take a closer look - iPhone 16 Pro & iPhone 16 Pro Max').click()
    popup_header = page.locator("//div[@id='panel-:r21:-0']//h2[@id='rf-digitalmat-overlay-label-0']")
    expect(popup_header).to_have_text('яблокофон 16 про')
