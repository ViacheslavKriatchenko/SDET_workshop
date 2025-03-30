import pytest
import allure

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FireService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FireOptions
from config.ConfigProvider import ConfigProvider


@pytest.fixture()
@allure.title('Подготовка к тесту, выбор браузера')
def driver():
    DRIVER_NAME = ConfigProvider().get(section='common', prop='BROWSER')
    if DRIVER_NAME == 'Chrome':
        options = ChromeOptions()
        options.add_argument('--headless')
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument(
            "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0"
        )
        service = ChromeService(executable_path=ChromeDriverManager().install())
        driver = webdriver.Chrome(options=options, service=service)
    elif DRIVER_NAME == 'Firefox':
        options = FireOptions()
        # options.add_argument('--headless')
        options.add_argument('--windowsize=1920,1080')
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument(
            "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0"
        )
        service = FireService(executable_path=GeckoDriverManager().install())
        driver = webdriver.Firefox(options=options, service=service)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
