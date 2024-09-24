import requests
import allure

from test_api_okarpuk.endpoints.endpoint import Endpoint


class DeletePost(Endpoint):

    @allure.step('Delete a post')
    def make_delete_post(self, post_id, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.delete(
            f'{self.url}/{post_id}',
            # json=payload,
            headers=headers
        )
        self.json = self.response.json()
        return self.response
