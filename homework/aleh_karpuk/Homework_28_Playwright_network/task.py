from playwright.sync_api import Page, expect, Request, Route, APIResponse
import re
import json
from time import sleep

def test_iphone_title_interception(page: Page):

    def modify_product_name(route: Route):
        response = route.fetch()
        body = response.json()
        body['body']['digitalMat'][0]['familyTypes'][0]['productName'] = 'яблокофон 16 про'
        body = json.dumps(body)
        route.fulfill(
            response=response,
            body=body)

    # https://www.apple.com/shop/api/digital-mat?path=library/step0_iphone/digitalmat
    page.route(re.compile('digitalmat$'), modify_product_name)


    page.goto('https://www.apple.com/shop/buy-iphone')
    page.get_by_role('button', name='Take a closer look - iPhone 16 Pro & iPhone 16 Pro Max').click()
    sleep(5)

    popup = page.get_by_role("heading", name='яблокофон 16 про', exact=True)


    # popup = page.locator('.rf-digitalmat-inlinetabnav-contentsection')


    expect(popup).to_have_text('яблокофон 16 про')

