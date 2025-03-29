class ManagerLocator:

    ADD_CUSTOMER = ('xpath', '//button[contains(text(), "Add Customer")]')
    FIRST_NAME_INPUT = ('xpath', '//input[@ng-model="fName"]')
    LAST_NAME_INPUT = ('xpath', '//input[@ng-model="lName"]')
    POST_CODE_INPUT = ('xpath', '//input[@ng-model="postCd"]')
    SUBMIT_ADD_CUSTOMER_BUTTON = ('xpath', '//button[@type="submit"]')

    CUSTOMERS_BUTTON = ('xpath', '//button[contains(text(), "Customers")]')
    FILTER_FIRST_NAME = ('xpath', '//table//a[contains(text(), "First Name")]')
    TABLE_DATA = ('xpath', '//table/tbody/tr')
    TABLE_CUSTOMERS_NAME_LIST = ('xpath', '//table//tr/td[1]')

    DELETE_BUTTON = ('xpath', '//button[contains(text(), "Delete")]')
