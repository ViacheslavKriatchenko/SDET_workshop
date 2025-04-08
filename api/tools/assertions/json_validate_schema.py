import allure

from typing import Any
from jsonschema import validate


@allure.step("Validating JSON schema")
def validate_json_schema(instance: Any, schema: dict) -> None:
    """"
    Проверяет, соответствует ли JSON-объект (instance) заданной JSON-схеме (schema).

    :param: instance (Any): JSON-объект, который необходимо проверить.
    :param: schema (dict): JSON-схема, согласно которой производится валидация.
    :raises:
        jsonschema.exceptions.ValidationError: В случае несоответствия JSON-объекта схеме.
        jsonschema.exceptions.SchemaError: Если переданная схема некорректна.
    """
    validate(instance=instance, schema=schema)
