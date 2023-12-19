import allure
import pytest
from pages.main_page import MainPage
from pages.order_page import OrderPage
from constants import urls
from constants import locators as loc


@pytest.mark.usefixtures('driver')
class TestTransitions:
    @allure.suite("Тесты переходов")
    @allure.title("Переход к странице заказа по клику на кнопку 'Заказать' в заголовке главной страницы")
    def test_header_order_button(self):
        self.driver.get(urls.url_main_page)
        main_page = MainPage(self.driver)
        main_page.go_to_header_order()
        assert main_page.current_url() == urls.url_order_page

    @allure.suite("Тесты переходов")
    @allure.title("Переход к странице заказа по клику на кнопку 'Заказать' в теле главной страницы")
    def test_body_order_button(self):
        self.driver.get(urls.url_main_page)
        main_page = MainPage(self.driver)
        main_page.go_to_body_order()
        assert main_page.current_url() == urls.url_order_page

    @allure.suite("Тесты переходов")
    @allure.title("Переход к Дзену по клику на 'Яндекс'")
    def test_yandex_link(self):
        self.driver.get(urls.url_main_page)
        main_page = MainPage(self.driver)
        main_page.follow_yandex_link()
        main_page.wait_number_of_windows(10, 2)
        main_page.change_window()
        main_page.wait_visibility(20, loc.DZEN_LOGO)
        assert 'dzen.ru' in main_page.current_url()

    @allure.suite("Тесты переходов")
    @allure.title("Переход к главной странице по клику на 'Самокат'")
    def test_return_to_main_page(self):
        self.driver.get(urls.url_order_page)
        order_page = OrderPage(self.driver)
        order_page.click_to_scooter()
        assert order_page.current_url() == urls.url_main_page
