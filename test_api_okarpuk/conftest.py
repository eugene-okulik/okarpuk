import pytest
import requests
from endpoints.create_post import CreatePost
from endpoints.update_post import UpdatePost
from endpoints.patch_post import PatchPost



@pytest.fixture()
def create_post_endpoint():
    return CreatePost()

@pytest.fixture()
def update_post_endpoint():
    return UpdatePost()

@pytest.fixture()
def patch_post_endpoint():
    return PatchPost()




@pytest.fixture()
def post_id(create_post_endpoint):
    payload = {"name": "ASUS Vivobook Pro 14X",
            "data": {"year": 2023, "price": 1500, "CPU model": "Intel Core i3", "Hard disk size": "500 GB"}}
    create_post_endpoint.create_new_post(payload)
    yield create_post_endpoint.post_id







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
