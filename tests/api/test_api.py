import allure
import pytest

from api.endpoints import create_object
from api.endpoints import get_object
from api.endpoints import get_getall_objects
from api.endpoints import patch_update_object
from api.endpoints import delete_object
from api.data.api_data import payloads
from api.tools.assertions.base import assert_status_code
from api.tools.assertions.json_validate_schema import validate_json_schema
from api.data.api_data.schemas import CreateObjectSchema


@allure.title("Создание объекта")
@pytest.mark.api
def test_create_object():
    create = create_object.CreateObject()
    validate_data = CreateObjectSchema(**payloads.body)

    create.create_object(payload=validate_data.model_dump())

    assert_status_code(actual=create.response.status_code, expected=200)
    validate_json_schema(instance=create.response_json, schema=create_object.CreateObjectSchema.Schema)


@allure.title("Подтверждение создания объекта")
@pytest.mark.api
def test_get_object(api_create_object):
    get = get_object.GetObject()
    id = api_create_object

    get.get_object_by_id(object_id=id)
    res_id = get.response_json['id']
    assert res_id == id
