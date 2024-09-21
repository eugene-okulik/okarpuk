import pytest
import requests


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
