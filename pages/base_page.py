from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def scroll_method(self, locator):
        button = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", button)

    def click_element(self, locator):
        self.driver.find_element(*locator).click()

    def fill_field(self, locator, value):
        self.driver.find_element(*locator).send_keys(value)

    def wait_visibility(self, timeout, locator):
        WebDriverWait(self.driver, timeout).until(expected_conditions.visibility_of_element_located(locator))

    def wait_clickable(self, timeout, locator):
        WebDriverWait(self.driver, timeout).until(expected_conditions.element_to_be_clickable(locator))

    def wait_number_of_windows(self, timeout, number):
        WebDriverWait(self.driver, timeout).until(expected_conditions.number_of_windows_to_be(number))

    def get_text(self, locator):
        return self.driver.find_element(*locator).text

    def current_url(self):
        return self.driver.current_url

    def change_window(self):
        new_page = self.driver.window_handles[1]
        self.driver.switch_to.window(new_page)
