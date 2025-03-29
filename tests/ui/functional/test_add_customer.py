from pages.ManagerPage.manager_page import ManagerPage


def test_add_customer(driver):
    manager = ManagerPage(driver)

    manager.open_the_page()
    manager.click_add_customer_button()
    code = manager.generate_N_number(10)
    manager.input_post_code(code=code)
    manager.input_first_name(code=code)
    manager.input_last_name()
    manager.click_add_customer_submit_button()
    alert_text = manager.switch_to_alert_and_take_text()

    assert "Customer added successfully" in alert_text


def test_soft_by_fname(driver):
    manager = ManagerPage(driver)

    manager.open_the_page()
    manager.click_customers_button()
    manager.click_filter_first_name()
    fName_list = manager.take_customers_list()

    assert fName_list == sorted(fName_list) or reversed(fName_list)


def test_delete_client(driver):
    manager = ManagerPage(driver)

    manager.open_the_page()
    manager.click_customers_button()
    avg_client_name = manager.search_avg_client_name()
    manager.remove_client(avg_client_name)

    assert avg_client_name not in manager.take_customers_list()
