import allure
import requests
from data.user_data import Data


class GetObjects:
    URL = Data.API_HOST
    response = None
    response_json = None

    @allure.step("GET request")
    def get_all_object(self):
        '''
        GET-запрос получения всех объектов

        :return None:
        '''
        self.response = requests.get(
            url=f'{self.URL}/api/getall'
        )
        self.response_json = self.response.json()
