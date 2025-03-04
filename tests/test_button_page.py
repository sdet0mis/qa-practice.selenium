import pytest
import allure

from pages.button_page import ButtonPage
from config.locators import ButtonPageLocators


@allure.title("Test click simple button")
@pytest.mark.smoke
def test_click_simple_button(driver):
    button_page = ButtonPage(driver)
    button_page.open_button_page()
    button_page.click_simple_button()
    assert driver.find_element(
        *ButtonPageLocators.RESULT_TEXT
    ).text == "Submitted"
