import allure

from pages.base_page import BasePage
from config.urls import URLs
from config.locators import ButtonPageLocators


class ButtonPage(BasePage):

    @allure.step("Open button page")
    def open_button_page(self):
        self.driver.get(URLs.BUTTON_PAGE)

    @allure.step("Click simple button")
    def click_simple_button(self):
        self.click(ButtonPageLocators.SIMPLE_BUTTON)
