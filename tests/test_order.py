import allure
import pytest
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pages.order_page import OrderPage

from constants import constants as const
from constants import locators as loc


class TestOrderPage:
    driver = None

    @classmethod
    def setup_class(cls):
        with allure.step('Открыть браузер'):
            cls.driver = webdriver.Firefox()

    @allure.suite("Тесты на странице оформления заказа")
    @allure.title("Оформление заказа")
    @pytest.mark.parametrize("name, lastname, address, station, phone_number, time, period, color, comment",
                             [const.first_set_list, const.second_set_list])
    def test_order(self, name, lastname, address, station, phone_number, time, period, color, comment):
        with allure.step("Открыть страницу оформления заказа"):
            self.driver.get(const.url_order_page)
        order_page = OrderPage(self.driver)
        with allure.step("Закрыть окно-уведомление о сборе куки, если оно присутствует"):
            try:
                self.driver.find_element(*loc.COOKIE_BUTTON).click()
            except NoSuchElementException:
                print('нет уведомления о сборе куки')
        order_page.first_order_page(name, lastname, address, station, phone_number)
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(loc.NEXT_BUTTON))
        order_page.click_next_button()
        WebDriverWait(self.driver, 10).until(expected_conditions.
                                             visibility_of_element_located(loc.SECOND_ORDER_PAGE_HEADER))
        order_page.second_order_page(time, period, color, comment)
        WebDriverWait(self.driver, 10).until(expected_conditions.
                                             visibility_of_element_located(loc.INFORMATION_ABOUT_ORDER))
        with allure.step("Проверить, что появилось сообщение 'Заказ оформлен'"):
            assert 'Заказ оформлен' in self.driver.find_element(*loc.DONE_ORDER_PAGE).text

    @allure.suite("Тесты на странице оформления заказа")
    @allure.title("Переход к главной странице по клику на 'Самокат'")
    def test_return_to_main_page(self):
        with allure.step("Открыть страницу оформления заказа"):
            self.driver.get(const.url_order_page)
        order_page = OrderPage(self.driver)
        order_page.click_to_scooter()
        with allure.step("Проверить, что произошел редирект на главную страницу"):
            assert self.driver.current_url == const.url_main_page

    @classmethod
    def teardown_class(cls):
        with allure.step('Закрыть браузер'):
            cls.driver.quit()
