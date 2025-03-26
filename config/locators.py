from selenium.webdriver.common.by import By


class InputPageLocators:

    TEXT_INPUT = (By.ID, "id_text_string")


class ButtonPageLocators:

    SIMPLE_BUTTON = (By.XPATH, "//input[@type='submit']")
    RESULT_TEXT = (By.ID, "result-text")
