from locust import task, HttpUser
import random


class MemeUser(HttpUser):
    token = None

    def on_start(self):
        response = self.client.post(
            '/auth/login',
            json={'username': "mor_2314",
                  'password': "83r5^_"}
        )
        self.token = response.json()['token']

    @task(1)
    def get_all_products(self):
        self.client.get(
            '/products',
            headers={'Authorization': self.token}
        )

    @task(2)
    def get_one_product(self):
        self.client.get(
            f'/products/{random.randint(1, 20)}',
            headers={'Authorization': self.token}
        )

    @task(2)
    def create_one_product(self):
        self.client.post(
            '/products',
            json={'title': 'test product',
                  'price': 13.5,
                  'description': 'lorem ipsum set'
                  },
            headers={'Authorization': self.token}
        )











