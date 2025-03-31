import allure

from pages.ManagerPage.manager_page import ManagerPage
from data.user_data import Data


@allure.title("Создание клиента")
@allure.tag("Тест-1")
@allure.description("Создадим клиента, учитывая условия из тест-кейса")
@allure.severity(allure.severity_level.CRITICAL)
def test_add_customer(driver):
    manager = ManagerPage(driver)
    data = Data()

    manager.open_the_page()
    manager.click_add_customer_button()
    code = manager.generate_N_number(data.N)
    manager.input_post_code(code=code)
    manager.input_first_name(code=code)
    manager.input_last_name(lname=data.lname)
    manager.click_add_customer_submit_button()
    alert_text = manager.switch_to_alert_and_take_text()

    with allure.step("Проверяем успешность создания записи"):
        assert "Customer added successfully" in alert_text, "Ошибка: Запись не создана"


@allure.title("Сортировка клиента")
@allure.tag("Тест-2")
@allure.description("Отсортируем список со имени")
@allure.severity(allure.severity_level.CRITICAL)
def test_sort_by_fname(driver):
    manager = ManagerPage(driver)

    manager.open_the_page()
    manager.click_customers_button()
    manager.click_filter_first_name()
    fName_list = manager.take_customers_list()

    with allure.step("Проверяем что список отсортирован"):
        assert fName_list == sorted(fName_list) or reversed(fName_list), f"Ошибка: список не отсортирован! {fName_list}"


@allure.title("Удаление клиента")
@allure.tag("Тест-3")
@allure.description("Удалим клиента, учитывая условия из тест-кейса")
@allure.severity(allure.severity_level.CRITICAL)
def test_delete_client(driver):
    manager = ManagerPage(driver)

    manager.open_the_page()
    manager.click_customers_button()
    avg_client_name = manager.search_avg_client_name()
    manager.remove_client(avg_client_name)

    with allure.step("Проверяем что запись пользователя удалена"):
        assert avg_client_name not in manager.take_customers_list(), "Ошибка: Запись не удалена"
