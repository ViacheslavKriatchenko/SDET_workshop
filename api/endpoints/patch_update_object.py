import allure
import requests
from data.user_data import Data


class UpdateObject:
    URL = Data.API_HOST
    response = None
    response_json = None

    @allure.step("PATCH request")
    def update_object_by_id(self, object_id, payload):
        '''
        PATCH-запрос изменения объекта

        :param object_id: id объекта
        :param payload: измененное тело запроса
        :return None: через атрибуты класса
        '''
        self.response = requests.patch(
            url=f'{self.URL}/api/patch/{object_id}',
            json=payload
        )
        try:
            self.response_json = self.response.json()
        except requests.JSONDecodeError:
            self.response_json = None
