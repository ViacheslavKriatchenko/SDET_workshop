import allure
import requests
from data.user_data import Data


class DeleteObject:

    URL = Data.API_HOST
    response = None
    response_json = None

    @allure.step("DELETE request")
    def delete_object_by_id(self, object_id):
        '''
        DELETE-запрос

        :param object_id: id
        :return None:
        '''
        self.response = requests.delete(
            url=f'{self.URL}/api/delete/{object_id}'
        )
        self.response_json = self.response.json()


class DeleteObjectSchema:

    Schema = {
        "type": "integer"
    }
