import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from constants import locators as loc


class MainPage:

    def __init__(self, driver):
        self.driver = driver

    def scroll_method(self, locator):
        button = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", button)

    @allure.step('Кликнуть на вопрос из списка "Вопросы о важном"')
    def get_answer(self, number_of_question):
        question, answer = loc.question_locator_constructor(number_of_question)
        self.scroll_method(question)
        WebDriverWait(self.driver, 15).until(expected_conditions.visibility_of_element_located(question))
        WebDriverWait(self.driver, 15).until(expected_conditions.element_to_be_clickable(question))
        self.driver.find_element(*question).click()
        WebDriverWait(self.driver, 15).until(expected_conditions.visibility_of_element_located(answer))
        return self.driver.find_element(*answer).text

    @allure.step('Кликнуть на кнопку "Заказать" в заголовке страницы')
    def go_to_header_order(self):
        self.scroll_method(loc.ORDER_HEADER_BUTTON)
        self.driver.find_element(*loc.ORDER_HEADER_BUTTON).click()
        WebDriverWait(self.driver, 10).until(expected_conditions.
                                             visibility_of_element_located(loc.FIRST_ORDER_PAGE_HEADER))

    @allure.step('Кликнуть на кнопку "Заказать" в теле страницы')
    def go_to_body_order(self):
        self.scroll_method(loc.ORDER_BODY_BUTTON)
        WebDriverWait(self.driver, 10).until(expected_conditions.
                                             visibility_of_element_located(loc.ORDER_BODY_BUTTON))
        WebDriverWait(self.driver, 10).until(expected_conditions.
                                             element_to_be_clickable(loc.ORDER_BODY_BUTTON))
        self.driver.find_element(*loc.ORDER_BODY_BUTTON).click()
        WebDriverWait(self.driver, 10).until(expected_conditions.
                                             visibility_of_element_located(loc.FIRST_ORDER_PAGE_HEADER))

    @allure.step('Кликнуть на "Яндекс" в заголовке страницы')
    def follow_yandex_link(self):
        self.driver.find_element(*loc.YANDEX_LINK).click()
