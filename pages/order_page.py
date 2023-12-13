import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from constants import locators as loc


class OrderPage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Заполнить поле "Имя"')
    def set_name(self, name):
        self.driver.find_element(*loc.NAME_FIELD).send_keys(name)

    @allure.step('Заполнить поле "Фамилия"')
    def set_lastname(self, lastname):
        self.driver.find_element(*loc.LASTNAME_FIELD).send_keys(lastname)

    @allure.step('Заполнить поле "Адрес"')
    def set_address(self, address):
        self.driver.find_element(*loc.ADDRESS_FIELD).send_keys(address)

    @allure.step('Заполнить поле "Станция метро"')
    def set_station(self, station):
        self.driver.find_element(*loc.STATION_FIELD).click()
        WebDriverWait(self.driver, 10).until(expected_conditions.
                                             visibility_of_element_located(loc.LIST_OF_STATION))
        self.driver.find_element(*loc.station_locator_constructor(station)).click()

    @allure.step('Заполнить поле "Телефон"')
    def set_phone(self, number):
        self.driver.find_element(*loc.PHONE_FIELD).send_keys(number)

    @allure.step('Заполнить поле "Когда привезти самокат?"')
    def set_delivery_time(self, time):
        self.driver.find_element(*loc.TIME_FIELD).send_keys(time)
        self.driver.find_element(*loc.BACKGROUND).click()

    @allure.step('Выбрать срок аренды')
    def choose_rental_period(self, period):
        self.driver.find_element(*loc.RENTAL_PERIOD_FIELD).click()
        WebDriverWait(self.driver, 10).until(expected_conditions.
                                             visibility_of_element_located(loc.LIST_OF_RENTAL_OPTIONS))
        self.driver.find_element(*loc.rental_locator_constructor(period)).click()

    @allure.step('Выбрать цвет самоката')
    def choose_color_of_scooter(self, color):
        self.driver.find_element(By.ID, color).click()

    @allure.step('Заполнить комментарий для курьера')
    def set_comment_for_deliverer(self, comment):
        self.driver.find_element(*loc.COMMENT_FIELD).send_keys(comment)

    @allure.step('Кликнуть на кнопку "Далее"')
    def click_next_button(self):
        self.driver.find_element(*loc.NEXT_BUTTON).click()

    @allure.step('Кликнуть на кнопку "Заказать"')
    def click_order_button(self):
        self.driver.find_element(*loc.ORDER_BUTTON).click()

    @allure.step('Кликнуть на кнопку "Да"')
    def click_yes_button(self):
        self.driver.find_element(*loc.YES_BUTTON).click()

    @allure.step('Кликнуть на "Самокат" в заголовке страницы')
    def click_to_scooter(self):
        self.driver.find_element(*loc.SCOOTER_LINK).click()

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
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(loc.ORDER_BUTTON))
        self.click_order_button()
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(loc.ORDER_CONFIRMATION_HEADER))
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(loc.YES_BUTTON))
        self.click_yes_button()
