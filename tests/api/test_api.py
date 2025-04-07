import allure
import pytest

from api.endpoints import create_object
from api.endpoints import get_object
from api.endpoints import get_getall_objects
from api.endpoints import patch_update_object
from api.endpoints import delete_object
from api.data.api_data import payloads
from api.tools.assertions.base import assert_status_code
from api.tools.assertions.base import assert_equal
from api.tools.assertions.json_validate_schema import validate_json_schema
from api.data.api_data.schemas import CreateObjectSchema
from api.data.api_data.schemas import ResponseGetObjectSchema


@allure.title("Создание объекта")
@pytest.mark.api
def test_create_object():
    create = create_object.CreateObject()
    validate_data = CreateObjectSchema(**payloads.body)

    create.create_object(payload=validate_data.model_dump())

    assert_status_code(actual=create.response.status_code, expected=200)
    validate_json_schema(instance=create.response_json, schema=create_object.CreateJsonObjectSchema.Schema)


@allure.title("Подтверждение создания объекта")
@pytest.mark.api
def test_get_object(api_create_object_fixture):
    get = get_object.GetObject()
    id, request_body = api_create_object_fixture

    get.get_object_by_id(object_id=id)
    res_id = get.response_json['id']

    assert_equal(actual=id, expected=res_id, name='id')
    assert_equal(actual=get.response_json['title'], expected=request_body['title'], name="title")
    assert_status_code(actual=get.response.status_code, expected=200)
    validate_json_schema(instance=get.response_json, schema=get_object.GetJsonObjectSchema.Schema)


@allure.title("Подтверждение создания объекта")
@pytest.mark.api
def test_getall_objects(api_create_object_fixture):
    getall = get_getall_objects.GetObjects()
    id = api_create_object_fixture[0]

    getall.get_all_object()
    validate_json_schema(instance=getall.response_json, schema=get_getall_objects.GetAllJsonObjectSchema.Schema)
    assert "entity" in getall.response_json
    assert id in getall.response_json


@allure.title("Обновление созданного объекта")
@pytest.mark.api
def test_update_object(api_create_object_fixture):
    update = patch_update_object.UpdateObject()
    get = get_object.GetObject()
    id = api_create_object_fixture[0]
    validate_data = CreateObjectSchema(**payloads.update_body).model_dump()

    get.get_object_by_id(object_id=id)
    before_body = ResponseGetObjectSchema(**get.response_json)

    update.update_object_by_id(object_id=id, payload=validate_data)
    get.get_object_by_id(object_id=id)
    after_body = ResponseGetObjectSchema(**get.response_json)

    assert before_body != after_body


@allure.title("Удаление созданного объекта объекта")
@pytest.mark.api
def test_delete_object(api_create_object_fixture):
    id = api_create_object_fixture[0]
    delete = delete_object.DeleteObject()

    delete.delete_object_by_id(object_id=id)

    assert_status_code(actual=delete.response.status_code, expected=204)
    assert_equal(actual=delete.response_json, expected=None)
