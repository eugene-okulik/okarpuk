import requests
import json


def post_an_object():
    body = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2024,
            "price": 1999.99,
            "CPU model": "Intel Core i7",
            "Hard disk size": "1 TB"
        }
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(
        'https://api.restful-api.dev/objects',
        json=body,
        headers=headers
    )
    assert response.status_code == 200, 'Status code is incorrect'
    assert response.json()['name'] == "Apple MacBook Pro 16", 'Name is incorrect'
    assert response.json()['data']['year'] == 2024, 'Year is incorrect'
    print("POST test PASSED")


def new_object():
    body = {
        "name": "ASUS Vivobook Pro 14X",
        "data": {
            "year": 2023,
            "price": 1500,
            "CPU model": "Intel Core i3",
            "Hard disk size": "500 GB"
        }
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(
        'https://api.restful-api.dev/objects',
        json=body,
        headers=headers
    )
    return response.json()['id']


def clear(post_id):
    requests.delete(f'https://api.restful-api.dev/objects/{post_id}')


def put_an_object():
    post_id = new_object()
    body = {
        "name": "Honor Magicbook X16",
        "data": {
            "year": 2022,
            "price": 1333,
            "CPU model": "Intel Core i5",
            "Hard disk size": "250 GB",
            "color": "silver"
        }
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.put(
        f'https://api.restful-api.dev/objects/{post_id}',
        json=body,
        headers=headers
    )
    assert response.status_code == 200, 'Status code is incorrect'
    assert response.json()['id'] == post_id, 'ID is incorrect'
    assert response.json()['name'] == 'Honor Magicbook X16', 'Name is incorrect'
    assert response.json()['data']['CPU model'] == 'Intel Core i5', 'CPU model is incorrect'
    clear(post_id)
    print("PUT test PASSED")


def patch_an_object():
    post_id = new_object()
    body = {
        "name": "Acer Aspire 5",
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.patch(
        f'https://api.restful-api.dev/objects/{post_id}',
        json=body,
        headers=headers
    )
    assert response.status_code == 200, 'Status code is incorrect'
    assert response.json()['id'] == post_id, 'ID is incorrect'
    assert response.json()['name'] == 'Acer Aspire 5', 'Name is incorrect'
    assert response.json()['data']['price'] == 1500, 'Price is incorrect'
    clear(post_id)
    print("PATCH test PASSED")


def delete_an_object():
    post_id = new_object()
    response = requests.delete(f'https://api.restful-api.dev/objects/{post_id}')
    assert response.status_code == 200, 'Status code is incorrect'
    assert response.json()['message'] == f'Object with id = {post_id} has been deleted.', 'Message is incorrect'
    print("DELETE test PASSED")


post_an_object()
put_an_object()
patch_an_object()
delete_an_object()
