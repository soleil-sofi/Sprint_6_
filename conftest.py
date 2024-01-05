import allure
import pytest
from selenium import webdriver
from pages.base_page import BasePage
from constants import locators as loc
from constants import urls


@pytest.fixture(scope="class", autouse=True)
def driver(request):
    with allure.step('Открыть браузер'):
        request.cls.driver = webdriver.Firefox()
    yield
    with allure.step('Закрыть браузер'):
        request.cls.driver.quit()


@pytest.fixture(scope="class")
def close_cookie_window(driver, request):
    request.cls.driver.get(urls.url_main_page)
    page = BasePage(request.cls.driver)
    page.wait_visibility(10, loc.COOKIE_BUTTON)
    page.wait_clickable(10, loc.COOKIE_BUTTON)
    page.click_element(loc.COOKIE_BUTTON)
