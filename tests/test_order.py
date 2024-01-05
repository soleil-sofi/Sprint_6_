import allure
import pytest
from pages.order_page import OrderPage
from constants import data, urls
from constants import locators as loc


@pytest.mark.usefixtures('driver', 'close_cookie_window')
class TestOrder:

    @allure.suite("Тесты оформления заказа")
    @allure.title("Оформление заказа")
    @pytest.mark.parametrize("name, lastname, address, station, phone_number, time, period, color, comment",
                             [data.first_set_list, data.second_set_list])
    def test_order(self, name, lastname, address, station, phone_number, time, period, color, comment):
        self.driver.get(urls.url_order_page)
        order_page = OrderPage(self.driver)
        order_page.first_order_page(name, lastname, address, station, phone_number)
        order_page.wait_clickable(10, loc.NEXT_BUTTON)
        order_page.click_next_button()
        order_page.wait_visibility(10, loc.SECOND_ORDER_PAGE_HEADER)
        order_page.second_order_page(time, period, color, comment)
        order_page.wait_visibility(10, loc.INFORMATION_ABOUT_ORDER)
        assert 'Заказ оформлен' in order_page.get_text(loc.DONE_ORDER_PAGE)
