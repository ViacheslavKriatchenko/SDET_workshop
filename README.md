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
1. Склонировать репозитой "git clone https://github.com/ViacheslavKriatchenko/Sky_final_Auto.git"
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
- ./config - настройка конфигурации
    - locators.py - класс локаторов
    - ConfigProvider.py - глобальные настройки
- ./pages - описание страниц сайта
- ./tests - тесты
    - test_UI.py - UI тесты
- conftest.py - фикстуры
- global_options.ini - глобальные переменные
- requirements.txt - настройка окружения
- user_data.json - пользовательские данные
- README.md - описание проекта

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