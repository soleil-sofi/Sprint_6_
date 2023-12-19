import allure
from selenium.webdriver.common.by import By
from constants import locators as loc
from pages.base_page import BasePage


class OrderPage(BasePage):

    @allure.step('Заполнить поле "Имя"')
    def set_name(self, name):
        self.fill_field(loc.NAME_FIELD, name)

    @allure.step('Заполнить поле "Фамилия"')
    def set_lastname(self, lastname):
        self.fill_field(loc.LASTNAME_FIELD, lastname)

    @allure.step('Заполнить поле "Адрес"')
    def set_address(self, address):
        self.fill_field(loc.ADDRESS_FIELD, address)

    @allure.step('Заполнить поле "Станция метро"')
    def set_station(self, station):
        self.click_element(loc.STATION_FIELD)
        self.wait_visibility(10, loc.LIST_OF_STATION)
        self.click_element(loc.station_locator_constructor(station))

    @allure.step('Заполнить поле "Телефон"')
    def set_phone(self, number):
        self.fill_field(loc.PHONE_FIELD, number)

    @allure.step('Заполнить поле "Когда привезти самокат?"')
    def set_delivery_time(self, time):
        self.fill_field(loc.TIME_FIELD, time)
        self.click_element(loc.BACKGROUND)

    @allure.step('Выбрать срок аренды')
    def choose_rental_period(self, period):
        self.driver.find_element(*loc.RENTAL_PERIOD_FIELD).click()
        self.wait_visibility(10, loc.LIST_OF_RENTAL_OPTIONS)
        self.click_element(loc.rental_locator_constructor(period))

    @allure.step('Выбрать цвет самоката')
    def choose_color_of_scooter(self, color):
        self.click_element((By.ID, color))

    @allure.step('Заполнить комментарий для курьера')
    def set_comment_for_deliverer(self, comment):
        self.fill_field(loc.COMMENT_FIELD, comment)

    @allure.step('Кликнуть на кнопку "Далее"')
    def click_next_button(self):
        self.click_element(loc.NEXT_BUTTON)

    @allure.step('Кликнуть на кнопку "Заказать"')
    def click_order_button(self):
        self.click_element(loc.ORDER_BUTTON)

    @allure.step('Кликнуть на кнопку "Да"')
    def click_yes_button(self):
        self.click_element(loc.YES_BUTTON)

    @allure.step('Кликнуть на "Самокат" в заголовке страницы')
    def click_to_scooter(self):
        self.click_element(loc.SCOOTER_LINK)

    def first_order_page(self, name, lastname, address, station, phone_number):
        self.set_name(name)
        self.set_lastname(lastname)
        self.set_address(address)
        self.set_station(station)
        self.set_phone(phone_number)

    def second_order_page(self, time, period, color, comment):
        self.set_delivery_time(time)
        self.choose_rental_period(period)
        self.choose_color_of_scooter(color)
        self.set_comment_for_deliverer(comment)
        self.wait_clickable(10, loc.ORDER_BUTTON)
        self.click_order_button()
        self.wait_visibility(10, loc.ORDER_CONFIRMATION_HEADER)
        self.wait_clickable(10, loc.YES_BUTTON)
        self.click_yes_button()
