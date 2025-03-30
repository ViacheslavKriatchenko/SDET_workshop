import allure

from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver, timeout=20) -> None:
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout=timeout, poll_frequency=1)

    @allure.step("Открыть страницу")
    def open_the_page(self) -> None:
        self.driver.get(self.PAGE_URL)

    @allure.step("Поиск элемента")
    def find_element(self, locator: tuple) -> WebElement:
        return self.wait.until(EC.visibility_of_element_located(locator),
                               message=f"element {locator} is not found")

    @allure.step("Поиск элементов")
    def find_elements(self, locator: tuple):
        return self.wait.until(EC.visibility_of_all_elements_located(locator),
                               message=f"element {locator} is not found")

    @allure.step("Действие клика")
    def click_element(self, element_locator: tuple) -> None:
        self.find_element(locator=element_locator).click()

    @allure.step("Ввод текста в выбранную область")
    def input_text(self, locator: tuple, text: str | int) -> str | int:
        self.find_element(locator=locator).send_keys(text)

    @allure.step("Действие с алерт окном")
    def switch_to_alert_and_take_text(self) -> str:
        alert = self.wait.until(EC.alert_is_present())
        self.driver.switch_to.alert
        text = alert.text
        alert.accept()
        return text
