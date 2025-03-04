from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout=10, poll_frequency=1)

    def fill_field(self, locator, data):
        return self.wait.until(EC.element_to_be_clickable(locator)).send_keys(
            data
        )

    def click(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator)).click()
