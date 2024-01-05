import allure
import pytest
from pages.main_page import MainPage
from constants import data, urls


@pytest.mark.usefixtures('driver')
class TestQuestions:

    @allure.suite("Тесты вопросов")
    @allure.title("Проверка 'Вопросов о важном'")
    @pytest.mark.parametrize("number_of_question", [0, 1, 2, 3, 4, 5, 6, 7])
    def test_list_of_questions(self, number_of_question):
        self.driver.get(urls.url_main_page)
        main_page = MainPage(self.driver)
        text_of_answer = main_page.get_answer(str(number_of_question))
        assert text_of_answer == data.expected_answers[number_of_question]
