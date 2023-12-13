import allure
import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions, wait
from selenium.webdriver.support.wait import WebDriverWait

from pages.main_page import MainPage
from constants import constants as const
from constants import locators as loc


class TestMainPage:
    driver = None

    @classmethod
    def setup_class(cls):
        with allure.step('Открыть браузер'):
            cls.driver = webdriver.Firefox()

    @allure.suite("Тесты на главной странице")
    @allure.title("Проверка 'Вопросов о важном'")
    @pytest.mark.parametrize("number_of_question", [0, 1, 2, 3, 4, 5, 6, 7])
    def test_list_of_questions(self, number_of_question):
        with allure.step("Открыть главную страницу"):
            self.driver.get(const.url_main_page)
        main_page = MainPage(self.driver)
        text_of_answer = main_page.get_answer(str(number_of_question))
        with allure.step("Проверить текст ответа на вопрос"):
            assert text_of_answer == const.expected_answers[number_of_question]

    @allure.suite("Тесты на главной странице")
    @allure.title("Переход к странице заказа по клику на кнопку 'Заказать' в заголовке главной страницы")
    def test_header_order_button(self):
        with allure.step("Открыть главную страницу"):
            self.driver.get(const.url_main_page)
        main_page = MainPage(self.driver)
        main_page.go_to_header_order()
        with allure.step("Проверить адрес текущей страницы"):
            assert self.driver.current_url == const.url_order_page

    @allure.suite("Тесты на главной странице")
    @allure.title("Переход к странице заказа по клику на кнопку 'Заказать' в теле главной страницы")
    def test_body_order_button(self):
        with allure.step("Открыть главную страницу"):
            self.driver.get(const.url_main_page)
        main_page = MainPage(self.driver)
        main_page.go_to_body_order()
        with allure.step("Проверить адрес текущей страницы"):
            assert self.driver.current_url == const.url_order_page

    @allure.suite("Тесты на главной странице")
    @allure.title("Переход к Дзену по клику на 'Яндекс'")
    def test_yandex_link(self):
        self.driver.get(const.url_main_page)
        main_page = MainPage(self.driver)
        main_page.follow_yandex_link()
        WebDriverWait(self.driver, 10).until(expected_conditions.number_of_windows_to_be(2))
        dzen = self.driver.window_handles[1]
        self.driver.switch_to.window(dzen)
        WebDriverWait(self.driver, 20).until(expected_conditions.visibility_of_element_located(loc.DZEN_LOGO))
        with allure.step("Проверить адрес текущей страницы"):
            assert 'dzen.ru' in self.driver.current_url

    @classmethod
    def teardown_class(cls):
        with allure.step('Закрыть браузер'):
            cls.driver.quit()
