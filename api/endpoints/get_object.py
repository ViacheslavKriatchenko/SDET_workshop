import allure
import requests
from data.user_data import Data


class GetObject:
    URL = Data.API_HOST
    response = None
    response_json = None

    @allure.step("GET request")
    def get_object_by_id(self, object_id: int):
        '''
        GET-запрос получения объекта

        :param object_id: id объекта
        :return None: через атрибуты класса
        '''
        self.response = requests.get(
            url=f'{self.URL}/api/get/{object_id}',
        )
        self.response_json = self.response.json()


class GetObjectSchema:

    Schema = {
        "type": "integer"
    }
