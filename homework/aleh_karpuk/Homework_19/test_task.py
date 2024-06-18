import requests
import json
import pytest


@pytest.fixture()
def new_object():
    body = {"name": "ASUS Vivobook Pro 14X",
            "data": {"year": 2023, "price": 1500, "CPU model": "Intel Core i3", "Hard disk size": "500 GB"}}
    headers = {'Content-Type': 'application/json'}
    response = requests.post(
        'https://api.restful-api.dev/objects',
        json=body,
        headers=headers
    )
    post_id = response.json()['id']
    print(post_id)
    yield post_id
    print('deleting the post')
    requests.delete(f'https://api.restful-api.dev/objects/{post_id}')


@pytest.fixture(scope='session')
def start_complete():
    print('\nStart testing')
    yield
    print('\nTesting completed')


@pytest.fixture()
def before_after_every_test():
    print('\nBefore test')
    yield
    print('\nAfter test')


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
    response = requests.post(
        'https://api.restful-api.dev/objects',
        json=body,
        headers=headers
    )
    assert response.status_code == 200, 'Status code is incorrect'


@pytest.mark.critical
def test_put_an_object(new_object, start_complete, before_after_every_test):
    body = {"name": "Honor Magicbook X16",
            "data": {"year": 2022,
                     "price": 1333,
                     "CPU model": "Intel Core i5",
                     "Hard disk size": "250 GB",
                     "color": "silver"}}
    headers = {'Content-Type': 'application/json'}
    response = requests.put(
        f'https://api.restful-api.dev/objects/{new_object}',
        json=body,
        headers=headers
    )
    assert response.status_code == 200, 'Status code is incorrect'
    assert response.json()['id'] == new_object, 'ID is incorrect'
    assert response.json()['name'] == 'Honor Magicbook X16', 'Name is incorrect'
    assert response.json()['data']['CPU model'] == 'Intel Core i5', 'CPU model is incorrect'


@pytest.mark.medium
def test_patch_an_object(new_object, start_complete, before_after_every_test):
    body = {"name": "Acer Aspire 5", }
    headers = {'Content-Type': 'application/json'}
    response = requests.patch(
        f'https://api.restful-api.dev/objects/{new_object}',
        json=body,
        headers=headers
    )
    assert response.status_code == 200, 'Status code is incorrect'
    assert response.json()['id'] == new_object, 'ID is incorrect'
    assert response.json()['name'] == 'Acer Aspire 5', 'Name is incorrect'
    assert response.json()['data']['price'] == 1500, 'Price is incorrect'


def test_delete_an_object(new_object, start_complete, before_after_every_test):
    response = requests.delete(f'https://api.restful-api.dev/objects/{new_object}')
    assert response.status_code == 200, 'Status code is incorrect'
    assert response.json()['message'] == f'Object with id = {new_object} has been deleted.', 'Message is incorrect'
