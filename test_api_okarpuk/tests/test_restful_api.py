import allure
import pytest
import requests


TEST_DATA = [
    {"name": "Apple MacBook Pro 16",
     "data": {"year": 2024,
               "price": 1999.99,
               "CPU model": "Intel Core i7",
               "Hard disk size": "1 TB"}},
     {"name": "Apple MacBook Air M1",
      "data": {"year": 2020,
               "price": 888.88,
               "CPU model": "Intel Core i3",
               "Hard disk size": "250 GB"}},
     {"name": "Apple MacBook Air M2",
      "data": {"year": 2020,
               "price": 1888.88,
               "CPU model": "Intel Core i5",
               "Hard disk size": "500 GB"}}
]

@allure.feature('Feature 1')
@allure.story('Story 1')
@allure.title('Test for Feature 1 and Story 1')
@pytest.mark.parametrize('data', TEST_DATA)
def test_post_a_post(create_post_endpoint, data):
    create_post_endpoint.create_new_post(payload=data)
    create_post_endpoint.check_that_status_is_200()
    create_post_endpoint.check_response_name_is_correct(data['name'])



@allure.feature('Feature 2')
@allure.story('Story 2')
@allure.title('Test for Feature 2 and Story 2')
@pytest.mark.critical
def test_put_a_post(update_post_endpoint, post_id):
    payload = {"name": "Honor Magicbook X16",
               "data": {"year": 2022,
                        "price": 1333,
                        "CPU model": "Intel Core i5",
                        "Hard disk size": "250 GB",
                        "color": "silver"}
               }
    update_post_endpoint.make_changes_in_post(post_id, payload)
    update_post_endpoint.check_that_status_is_200()
    update_post_endpoint.check_response_title_is_correct(payload['name'])



@allure.feature('Feature 3')
@allure.story('Story 3')
@allure.title('Test for Feature 3 and Story 3')
@pytest.mark.medium
def test_patch_a_post(patch_post_endpoint, post_id):
    payload = {"name": "Acer Aspire 5", }
    patch_post_endpoint.make_patch_in_post(post_id, payload)
    patch_post_endpoint.check_that_status_is_200()
    patch_post_endpoint.check_response_title_is_correct(payload['name'])


