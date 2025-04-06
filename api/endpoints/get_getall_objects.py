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


class GetAllJsonObjectSchema:

    Schema = {
        "type": "object",
        "properties": {
            "entity": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "integer"},
                        "title": {"type": "string"},
                        "verified": {"type": "boolean"},
                        "addition": {
                            "type": "object",
                            "properties": {
                                "id": {"type": "integer"},
                                "additional_info": {"type": "string"},
                                "additional_number": {"type": "integer"}
                            },
                            "required": ["id", "additional_info", "additional_number"],
                            "additionalProperties": False
                        },
                        "important_numbers": {
                            "type": "array",
                            "items": {
                                "type": "integer"
                                }
                        }
                    },
                    "required": ["id", "title", "verified", "addition", "important_numbers"],
                    "additionalProperties": False
                }
            }
        },
        "required": ["entity"],
        "additionalProperties": False
    }
