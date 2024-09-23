import pytest
from endpoints.create_post import CreatePost
from endpoints.update_post import UpdatePost
from endpoints.delete_post import DeletePost


@pytest.fixture()
def create_post_endpoint():
    return CreatePost()


@pytest.fixture()
def update_post_endpoint():
    return UpdatePost()


@pytest.fixture()
def delete_post_endpoint():
    return DeletePost()


@pytest.fixture()
def post_id(create_post_endpoint):
    payload = {"title": "test product 1", "price": 100, "description": "the best product"}
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
