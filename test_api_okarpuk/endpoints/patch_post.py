import requests
import allure
from test_api_okarpuk.endpoints.endpoint import Endpoint


class PatchPost(Endpoint):

    @allure.step('Patch a post')
    def make_patch_in_post(self, post_id, payload, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.patch(
            f'{self.url}/{post_id}',
            json=payload,
            headers=headers
        )
        self.json = self.response.json()
        return self.response
