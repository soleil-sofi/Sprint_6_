import allure
from constants import locators as loc
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step('Кликнуть на вопрос из списка "Вопросы о важном"')
    def get_answer(self, number_of_question):
        question, answer = loc.question_locator_constructor(number_of_question)
        self.scroll_method(question)
        self.wait_visibility(15, question)
        self.wait_clickable(15, question)
        self.click_element(question)
        self.click_element(answer)
        return self.get_text(answer)

    @allure.step('Кликнуть на кнопку "Заказать" в заголовке страницы')
    def go_to_header_order(self):
        self.scroll_method(loc.ORDER_HEADER_BUTTON)
        self.click_element(loc.ORDER_HEADER_BUTTON)
        self.wait_visibility(10, loc.FIRST_ORDER_PAGE_HEADER)

    @allure.step('Кликнуть на кнопку "Заказать" в теле страницы')
    def go_to_body_order(self):
        self.scroll_method(loc.ORDER_BODY_BUTTON)
        self.wait_visibility(10, loc.ORDER_BODY_BUTTON)
        self.wait_clickable(15, loc.ORDER_BODY_BUTTON)
        self.click_element(loc.ORDER_BODY_BUTTON)
        self.wait_visibility(10, loc.FIRST_ORDER_PAGE_HEADER)

    @allure.step('Кликнуть на "Яндекс" в заголовке страницы')
    def follow_yandex_link(self):
        self.click_element(loc.YANDEX_LINK)
