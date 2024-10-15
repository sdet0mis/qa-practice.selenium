import pytest
from selenium import webdriver

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.get('https://www.qa-practice.com/elements/button/simple')
    yield driver
    driver.quit()