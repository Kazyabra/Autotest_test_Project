# pytest -v --tb=line --language=en test_main_page.py
# pytest -v --tb=line --language=en -m login_guest test_main_page.py

import pytest
from .pages.locators import MainPageLocators
from .pages.base_page import BasePage
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage


@pytest.mark.login_guest
class TestLoginFromMainPage:
    def test_guest_should_see_login_link(self, browser):
        # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page = MainPage(browser, MainPageLocators.MAIN_PAGE_LINK)
        # открываем страницу
        page.open()
        # выполняем метод страницы - ищем ссылку на страницу логина
        page.should_be_login_link()

    def test_guest_can_go_to_login_page(self, browser):
        # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        main_page = MainPage(browser, MainPageLocators.MAIN_PAGE_LINK)
        # открываем страницу
        main_page.open()
        # выполняем метод страницы - переходим на страницу логина
        main_page.go_to_login_page()
        # инициализируем Page Object, передаем в конструктор экземпляр драйвера и текущий url адрес
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    """
    1. Гость открывает главную страницу
    2. Переходит в корзину по кнопке в шапке сайта
    3. Ожидаем, что в корзине нет товаров
    4. Ожидаем, что есть текст о том что корзина пуста
    """
    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page = MainPage(browser, MainPageLocators.MAIN_PAGE_LINK)
    # [1] открываем страницу
    page.open()
    # [2] выполняем метод страницы base page - переходим на страницу корзины
    page.go_to_basket_page()
    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и текущий url адрес
    page = BasketPage(browser, browser.current_url)
    # [3] проверяем, что в корзине нет товаров
    # ставит ожидание в 1сек
    page.browser.implicitly_wait(1)
    page.should_not_be_order_total_price()
    # ставит ожидание в 10сек
    page.browser.implicitly_wait(10)
    # [4] проверяем, что есть текст, о том, что корзина пуста
    page.should_be_message_basket_empty()


if __name__ == '__main__':
    pytest.main()
