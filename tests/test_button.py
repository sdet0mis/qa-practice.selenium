from selenium.webdriver.common.by import By


def test_button_exist(driver):
    assert driver.find_element(By.ID, 'submit-id-submit').is_displayed()


''' def test_button_clicked(driver):
    driver.find_element(By.ID, 'submit-id-submit').click()
    assert 'Submitted' == driver.find_element(By.ID, 'result-text').text'''
