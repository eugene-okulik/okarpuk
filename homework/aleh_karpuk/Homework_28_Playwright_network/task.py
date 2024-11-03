from playwright.sync_api import Page, expect, Request, Route, APIResponse
import re
import json
from time import sleep

def test_iphone_title_interception(page: Page):

    def modify_product_name(route: Route):
        response = route.fetch()
        body = response.json()

 
        body['partNumber'] = 'яблокофон 16 про'

        # for product in body.get('partNumber', []):
        #     if product.get('partNumber') == "iPhone 16 Pro":
        #         product['partNumber'] = "яблокофон 16 про"
        #         break


        body = json.dumps(body)
        route.fulfill(
            response=response,
            body=body)

    # https://www.apple.com/shop/api/digital-mat?path=library/step0_iphone/digitalmat
    page.route(re.compile('digital-mat'), modify_product_name)


    page.goto('https://www.apple.com/shop/buy-iphone')
    page.get_by_role('button', name='Take a closer look - iPhone 16 Pro & iPhone 16 Pro Max').click()
    sleep(5)

    popup = page.get_by_role("heading", name='iPhone 16 Pro', exact=True)
    expect(popup).to_have_text('яблокофон 16 про')

