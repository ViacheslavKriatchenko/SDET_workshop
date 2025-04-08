# "SDET_workshop"
### Практикум SDET: Задание UI
### Задание

- [] Составить подробные тест-кейсы по чек-листу из 3 кейсов
- [] *Реализовать параллельный запуск тестов
- [] *Реализовать запуск в системе CI/CD  
  
- [] Создать проект локально
- [] Создать репозиторий
- [] Создать первый коммит
- [] Инифиализировать репозиторий
- [] Построить структуру проекта
- [] Настроить Pytest
- [] Настроить Allure
- [] Прогнать локально
- [] Написать базовый .github/workflows/config.yml
- [] Написать полный конфиг для хранения запусковы

### Шаги:
1. Склонировать репозитой "git clone https://github.com/ViacheslavKriatchenko/SDET_workshop.git"
2. Запустить виртуальное окружение "python -m venv venv"
3. Установить окружение "python -m pip install -r requirements.txt"
4. Запустить тесты "pytest -s -v --alluredir allure_results"
5. Запустить тесты в несколько потоков pytest -n 2  # запуск в 2 потока
6. Просмотреть отчет "allure serve allure_results"

### Стэк:
- Selenium
- Webdriver-manager
- PyTest
- Allure

### Структура:
- ./.github/workflows
    - ci_tests.yml - настройки CI
    - api-tests.yml - настройки CI
- ./api
    - data
        - payloads.py - данные загрузки
        - schemas.py - pydantic схема проверки
    - endpoints - эндпоинты сервиса
    - tools/assertions
        - base.py - базовые проверки
        - json_validate_schema.py - функция валидации
- ./config - настройка конфигурации
    - ConfigProvider.py - глобальные 
- ./data - тестовые данные
    - user_data.py
- ./helpers - вспомогательные функции
    - functions.py
- ./pages - описание страниц сайта
- ./tests - тесты
    - api
        - conftest.py
        - test_api.py
    - ui
        - test_UI.py - UI тесты
- ./.gitignore
- conftest.py - фикстуры
- global_options.ini - глобальные переменные
- pytest.ini - настройки pytest
- README.md - описание проекта
- requirements.txt - настройка окружения
- Test_cases.md - тестовые сценарии

### Полезные ссылки:
[Гайд по Markdown](https://www.markdownguide.org/basic-syntax/)  
[Сайт генератор .gitignore](https://www.toptal.com/developers/gitignore)  
[Перенос окружения](https://pip.pypa.io/en/stable/cli/pip_freeze/)  
[Вызов PyTest инструкция](https://pytest-docs-ru.readthedocs.io/ru/latest/usage.html)

### Библиотеки:
- pip install selenium
- pip install webdriver-manager
- pip install pytest
- pip install requests
- pip install allure-pytest
- pip install pytest-xdist
- pip install pydantic
- pip install jsonschema
- pip install Faker