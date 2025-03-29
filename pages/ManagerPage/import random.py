from selenium import webdriver
import time


driver = webdriver.Chrome()

driver.get('https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager/list')
time.sleep(5)

TABLE_CUSTOMERS_NAME_LIST = ('xpath', '//table//tr/td[1]')

name_elements_list = driver.find_elements(*TABLE_CUSTOMERS_NAME_LIST)
names_list = [name.text for name in name_elements_list if name.text != "First Name"]
print(names_list)
name_length_list = [len(name) for name in names_list]
print(name_length_list)
avg_length = sum(name_length_list) / len(name_elements_list)
print(avg_length)
closest_name = min(names_list, key=lambda name: abs(len(name)) - avg_length)
print(*closest_name)

locator = f'("xpath", "//td[text()="{closest_name}"]/following-sibling::td/button[contains(text(), "Delete")]")'
print(locator)

driver.quit()
