import allure
import pytest


@pytest.mark.ui
@allure.title("Создание клиента")
@allure.tag("Тест-1")
@allure.description("Создадим клиента, учитывая условия из тест-кейса")
@allure.severity(allure.severity_level.CRITICAL)
def test_add_customer(manager, data):
    '''
    Этот тест преобразует данные и проверяет что клиент создался
    This test converts the data and verifies that the client has been created
    '''
    manager.open_the_page()
    manager.click_add_customer_button()
    code = manager.generate_N_number(data.N)
    manager.input_post_code(code=code)
    name = manager.input_first_name(code=code)
    manager.input_last_name(lname=data.lname)
    manager.click_add_customer_submit_button()
    alert_text = manager.switch_to_alert_and_take_text()

    with allure.step("Проверяем успешность создания записи"):
        assert "Customer added successfully" in alert_text, "Ошибка: Запись не создана"
    with allure.step("Проверяем что созданная запись находится в таблице"):
        manager.click_customers_button()
        assert name in manager.take_customers_list()


@pytest.mark.smoke
@allure.title("Сортировка клиента")
@allure.tag("Тест-2")
@allure.description("Отсортируем список со имени")
@allure.severity(allure.severity_level.CRITICAL)
def test_sort_by_fname(manager):
    manager.open_the_page()
    manager.click_customers_button()
    manager.click_filter_first_name()
    fName_list = manager.take_customers_list()

    with allure.step("Проверяем что список отсортирован"):
        assert fName_list == sorted(fName_list) or reversed(fName_list), f"Ошибка: список не отсортирован! {fName_list}"


@pytest.mark.ui
@allure.title("Удаление клиента")
@allure.tag("Тест-3")
@allure.description("Удалим клиента, учитывая условия из тест-кейса")
@allure.severity(allure.severity_level.CRITICAL)
def test_delete_client(manager):
    manager.open_the_page()
    manager.click_customers_button()
    avg_client_name = manager.search_avg_client_name()
    for _ in avg_client_name:
        manager.remove_client(_)

    with allure.step("Проверяем что запись пользователя удалена"):
        assert avg_client_name not in manager.take_customers_list(), "Ошибка: Запись не удалена"
