import allure
import requests
from data.user_data import Data


class CreateObject:
    URL = Data.API_HOST
    response = None
    response_json = None

    @allure.step("POST request")
    def create_object(self, payload) -> str:
        '''
        POST-запрос

        :param payload: тело запроса
        :return None: через аргументы класса
        '''
        self.response = requests.post(
            url=f'{self.URL}api/create',
            json=payload
        )
        self.response_json = self.response.json()


class CreateJsonObjectSchema:

    Schema = {
        "type": "integer"
    }
