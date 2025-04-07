import pytest

from api.endpoints import create_object
from api.data.api_data import payloads
from api.tools.assertions.base import assert_status_code
from api.tools.assertions.json_validate_schema import validate_json_schema
from api.data.api_data.schemas import CreateObjectSchema


@pytest.fixture
def api_create_object_fixture():
    '''
    создание объекта

    :return response, body: возврат ответ в виде id и тело запроса
    '''
    create = create_object.CreateObject()
    validate_data = CreateObjectSchema(**payloads.body)

    create.create_object(payload=validate_data.model_dump())

    assert_status_code(actual=create.response.status_code, expected=200)
    validate_json_schema(instance=create.response_json, schema=create_object.CreateJsonObjectSchema.Schema)
    return create.response_json, validate_data.model_dump()
