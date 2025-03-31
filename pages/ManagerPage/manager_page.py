import allure
import random
import string

from config.BasePage import BasePage
from .manager_page_locators import ManagerLocator
from data.user_data import Data


class ManagerPage(BasePage):

    PAGE_URL = Data().URL
    Locators = ManagerLocator()

    @allure.step("Кликаем по кнопке 'Add Customer")
    def click_add_customer_button(self) -> None:
        self.click_element(self.Locators.ADD_CUSTOMER)

    @allure.step("Генерируем N-значное число")
    def generate_N_number(self, N: int) -> int:
        if N < 1:
            raise ValueError("Количество цифр не может быть меньше 1")
        return f"{random.randint(0, 10**N - 1):0{N}d}"

    @allure.step("Преобразуем число в текст")
    def number_to_letters(self, number: int) -> str:
        number = str(number)
        alphabet = string.ascii_lowercase

        pairs = [int(number[i:i+2]) for i in range(0, len(number), 2)]
        letters = ''.join(alphabet[pair % 26] for pair in pairs)
        return letters

    @allure.step("Ввод текста в поле 'First Name'")
    def input_first_name(self, code: int) -> str:
        name = self.number_to_letters(number=code)
        self.input_text(locator=self.Locators.FIRST_NAME_INPUT, text=name)

    @allure.step("Ввод кода в поле 'Post Code'")
    def input_post_code(self, code: int) -> int:
        self.input_text(self.Locators.POST_CODE_INPUT, text=code)

    @allure.step("Ввод текста в поле 'Last Name'")
    def input_last_name(self, lname) -> str:
        self.input_text(self.Locators.LAST_NAME_INPUT, text=lname)

    @allure.step("Создаем запись нажатием кнопки 'Add Customer'")
    def click_add_customer_submit_button(self) -> None:
        self.click_element(
            element_locator=self.Locators.SUBMIT_ADD_CUSTOMER_BUTTON
            )

    @allure.step("Кликаем по кнопке 'Customers'")
    def click_customers_button(self) -> None:
        self.click_element(self.Locators.CUSTOMERS_BUTTON)

    @allure.step("Кликаем по кнопке фильтра 'First Name'")
    def click_filter_first_name(self) -> None:
        self.click_element(self.Locators.FILTER_FIRST_NAME)

    @allure.step("Создаем список пользователей по имени")
    def take_customers_list(self) -> list:
        table = self.find_elements(self.Locators.TABLE_DATA)
        all_table_texts = [data.text for data in table]
        fName_list = [res.split()[0] for res in all_table_texts]
        return fName_list

    @allure.step("Находим ближайшее имя согласно средней длины имен таблицы")
    def search_avg_client_name(self) -> str:
        names_elements_list = self.find_elements(
            self.Locators.TABLE_CUSTOMERS_NAME_LIST
            )
        names_list = [name.text for name in names_elements_list if name.text != "First Name"]

        names_length_list = [len(name) for name in names_list]
        avg_length = sum(names_length_list) / len(names_elements_list)

        closest_name = min(
            names_list, key=lambda name: abs(len(name)) - avg_length
            )
        return closest_name

    @allure.step("Удаляем запись имени {closest_name} нажатием кнопки 'Delete'")
    def remove_client(self, closest_name) -> None:
        delete_xpath_button = f'//td[text()="{closest_name}"]/following-sibling::td/button[contains(text(), "Delete")]'
        DELETE_BUTTON = self.driver.find_element('xpath', delete_xpath_button)
        DELETE_BUTTON.click()
