import random
import string

from config.BasePage import BasePage
from .manager_page_locators import ManagerLocator


class ManagerPage(BasePage):

    PAGE_URL = "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager"
    Locators = ManagerLocator()

    def click_add_customer_button(self):
        self.click_element(self.Locators.ADD_CUSTOMER)

    def generate_N_number(self, N: int) -> int:
        if N < 1:
            raise ValueError("Количество цифр не может быть меньше 1")
        return f"{random.randint(0, 10**N - 1):0{N}d}"

    def number_to_letters(self, number: int) -> str:
        number = str(number)
        alphabet = string.ascii_lowercase

        pairs = [int(number[i:i+2]) for i in range(0, len(number), 2)]
        letters = ''.join(alphabet[pair % 26] for pair in pairs)
        return letters

    def input_first_name(self, code: int) -> str:
        name = self.number_to_letters(number=code)
        self.input_text(locator=self.Locators.FIRST_NAME_INPUT, text=name)

    def input_post_code(self, code: int) -> int:
        self.input_text(self.Locators.POST_CODE_INPUT, text=code)

    def input_last_name(self) -> str:
        self.input_text(self.Locators.LAST_NAME_INPUT, text="Siblicus")

    def click_add_customer_submit_button(self):
        self.click_element(
            element_locator=self.Locators.SUBMIT_ADD_CUSTOMER_BUTTON
            )

    def click_customers_button(self):
        self.click_element(self.Locators.CUSTOMERS_BUTTON)

    def click_filter_first_name(self):
        self.click_element(self.Locators.FILTER_FIRST_NAME)

    def take_customers_list(self) -> list:
        table = self.find_elements(self.Locators.TABLE_DATA)
        all_table_texts = [data.text for data in table]
        fName_list = [res.split()[0] for res in all_table_texts]
        return fName_list

    def search_avg_client_name(self):
        names_elements_list = self.find_elements(self.Locators.TABLE_CUSTOMERS_NAME_LIST)
        names_list = [name.text for name in names_elements_list if name.text != "First Name"]

        names_length_list = [len(name) for name in names_list]
        avg_length = sum(names_length_list) / len(names_elements_list)

        closest_name = min(names_list, key=lambda name: abs(len(name)) - avg_length)

        return closest_name

    def remove_client(self, closest_name):
        delete_xpath_button = f'//td[text()="{closest_name}"]/following-sibling::td/button[contains(text(), "Delete")]'
        DELETE_BUTTON = self.driver.find_element('xpath', delete_xpath_button)
        DELETE_BUTTON.click()
