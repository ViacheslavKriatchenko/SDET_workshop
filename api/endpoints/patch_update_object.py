import requests
from data.user_data import Data


class UpdateObject:
    URL = Data.API_HOST
    response = None
    response_json = None

    def update_object_by_id(self, object_id, payload):
        self.response = requests.patch(
            url=f'{self.URL}/api/patch/{object_id}',
            payload=payload
        )
        self.response_json = self.response.json()
