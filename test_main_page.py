# pytest -v --tb=line --language=en test_main_page.py

import pytest
from .pages.main_page import MainPage
from .pages.locators import MainPageLocators
from .pages.login_page import LoginPage


def test_guest_should_see_login_link(browser):
    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page = MainPage(browser, MainPageLocators.MAIN_PAGE_LINK)
    # открываем страницу
    page.open()
    # выполняем метод страницы - ищем ссылку на страницу логина
    page.should_be_login_link()


def test_guest_can_go_to_login_page(browser):
    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    main_page = MainPage(browser, MainPageLocators.MAIN_PAGE_LINK)
    # открываем страницу
    main_page.open()
    # выполняем метод страницы - переходим на страницу логина
    main_page.go_to_login_page()
    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и текущий url адрес
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


if __name__ == '__main__':
    pytest.main()
