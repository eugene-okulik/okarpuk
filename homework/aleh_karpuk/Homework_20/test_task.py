import requests
import json
import pytest
import allure


@allure.feature('Feature 1')
@allure.story('Story 1')
@allure.title('Test for Feature 1 and Story 1')
@pytest.mark.parametrize('body', [{"name": "Apple MacBook Pro 16",
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
                                            "Hard disk size": "500 GB"}}])
def test_post_an_object(body, start_complete, before_after_every_test):
    headers = {'Content-Type': 'application/json'}
    with allure.step('Create an object with post method'):
        response = requests.post(
            'https://api.restful-api.dev/objects',
            json=body,
            headers=headers
        )
    with allure.step('Check that status code is 200'):
        assert response.status_code == 200, 'Status code is incorrect'


@allure.feature('Feature 2')
@allure.story('Story 2')
@allure.title('Test for Feature 2 and Story 2')
@pytest.mark.critical
def test_put_an_object(new_object, start_complete, before_after_every_test):
    body = {"name": "Honor Magicbook X16",
            "data": {"year": 2022,
                     "price": 1333,
                     "CPU model": "Intel Core i5",
                     "Hard disk size": "250 GB",
                     "color": "silver"}}
    headers = {'Content-Type': 'application/json'}
    with allure.step('Change an object with put method'):
        response = requests.put(
            f'https://api.restful-api.dev/objects/{new_object}',
            json=body,
            headers=headers
        )
    with allure.step('Check that status code is 200'):
        assert response.status_code == 200, 'Status code is incorrect'
    with allure.step(f'Check that ID is {new_object}'):
        assert response.json()['id'] == new_object, 'ID is incorrect'
    with allure.step('Check the name'):
        assert response.json()['name'] == 'Honor Magicbook X16', 'Name is incorrect'
    with allure.step('Check the CPU model'):
        assert response.json()['data']['CPU model'] == 'Intel Core i5', 'CPU model is incorrect'


@allure.feature('Feature 3')
@allure.story('Story 3')
@allure.title('Test for Feature 3 and Story 3')
@pytest.mark.medium
def test_patch_an_object(new_object, start_complete, before_after_every_test):
    body = {"name": "Acer Aspire 5", }
    headers = {'Content-Type': 'application/json'}
    with allure.step('Change an object with patch method'):
        response = requests.patch(
            f'https://api.restful-api.dev/objects/{new_object}',
            json=body,
            headers=headers
        )
    with allure.step('Check that status code is 200'):
        assert response.status_code == 200, 'Status code is incorrect'
    with allure.step(f'Check that ID is {new_object}'):
        assert response.json()['id'] == new_object, 'ID is incorrect'
    with allure.step('Check the name'):
        assert response.json()['name'] == 'Acer Aspire 5', 'Name is incorrect'
    with allure.step('Check the price'):
        assert response.json()['data']['price'] == 1500, 'Price is incorrect'


@allure.feature('Feature 4')
@allure.story('Story 4')
@allure.title('Test for Feature 4 and Story 4')
def test_delete_an_object(new_object, start_complete, before_after_every_test):
    with allure.step('Delete the object'):
        response = requests.delete(f'https://api.restful-api.dev/objects/{new_object}')
    with allure.step('Check that status code is 200'):
        assert response.status_code == 200, 'Status code is incorrect'
    with allure.step('Check the delete message'):
        assert response.json()['message'] == f'Object with id = {new_object} has been deleted.', 'Message is incorrect'
