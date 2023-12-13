from selenium.webdriver.common.by import By


def question_locator_constructor(n):
    return (By.ID, f'accordion__heading-{n}'), (By.ID, f'accordion__panel-{n}')


def rental_locator_constructor(period):
    return By.XPATH, f'.//div[@class="Dropdown-menu"]/div[text()="{period}"]'


def station_locator_constructor(station):
    return By.XPATH, f'.//ul[@class ="select-search__options"]/li[{station}]'


ORDER_HEADER_BUTTON = (By.XPATH, './/div[@class = "Header_Nav__AGCXC"]/button[text() = "Заказать"]')
ORDER_BODY_BUTTON = (By.XPATH, './/div[@class = "Home_FinishButton__1_cWm"]/button[text() = "Заказать"]')
COOKIE_BUTTON = (By.CLASS_NAME, 'App_CookieButton__3cvqF')
NEXT_BUTTON = (By.XPATH, './/div[@class = "Order_NextButton__1_rCA"]/button[text() = "Далее"]')
ORDER_BUTTON = (By.XPATH, './/div[@class = "Order_Buttons__1xGrp"]/button[text() = "Заказать"]')
YES_BUTTON = (By.XPATH, './/button[text()="Да"]')
YANDEX_LINK = (By.CLASS_NAME, 'Header_LogoYandex__3TSOI')
DZEN_LOGO = (By.XPATH, './/a[@data-testid = "logo"]')
SCOOTER_LINK = (By.CLASS_NAME, 'Header_LogoScooter__3lsAR')
NAME_FIELD = (By.XPATH, './/input[@placeholder = "* Имя"]')
LASTNAME_FIELD = (By.XPATH, './/input[@placeholder = "* Фамилия"]')
ADDRESS_FIELD = (By.XPATH, './/input[@placeholder = "* Адрес: куда привезти заказ"]')
STATION_FIELD = (By.XPATH, './/input[@placeholder = "* Станция метро"]')
LIST_OF_STATION = (By.CLASS_NAME, 'select-search__select')
PHONE_FIELD = (By.XPATH, './/input[@placeholder = "* Телефон: на него позвонит курьер"]')
FIRST_ORDER_PAGE_HEADER = (By.XPATH, './/div[text() = "Для кого самокат"]')
SECOND_ORDER_PAGE_HEADER = (By.XPATH, './/div[text() = "Про аренду"]')
TIME_FIELD = (By.XPATH, './/input[@placeholder = "* Когда привезти самокат"]')
BACKGROUND = (By.CLASS_NAME, 'Order_Content__bmtHS')
RENTAL_PERIOD_FIELD = (By.CLASS_NAME, 'Dropdown-control')
LIST_OF_RENTAL_OPTIONS = (By.CLASS_NAME, 'Dropdown-menu')
COMMENT_FIELD = (By.XPATH, './/input[@placeholder = "Комментарий для курьера"]')
ORDER_CONFIRMATION_HEADER = (By.CLASS_NAME, 'Order_ModalHeader__3FDaJ')
INFORMATION_ABOUT_ORDER = (By.XPATH, './/div[contains(text(), "Номер заказа")]')
DONE_ORDER_PAGE = (By.CLASS_NAME, 'Order_ModalHeader__3FDaJ')
