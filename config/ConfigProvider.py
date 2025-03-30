import allure
import configparser

global_config = configparser.ConfigParser()
global_config.read('global_options.ini')


class ConfigProvider:

    def __init__(self) -> None:
        self.config = global_config

    @allure.step("Получение данных в формате str")
    def get(self, section: str, prop: str) -> str:
        return self.config.get(section, prop)

    @allure.step("Получение данных в формате int")
    def getint(self, section: str, prop: str) -> int:
        return self.config.getint(section, prop)
