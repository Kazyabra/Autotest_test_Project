# pytest -v --tb=line --language=en test_main_page.py

import pytest
from .pages.login_page import LoginPage
from .pages.locators import LoginPageLocators


def test_guest_txt_login_is_url(browser):
    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page = LoginPage(browser, LoginPageLocators.LOGIN_PAGE_LINK)
    # открываем страницу
    page.open()
    # выполняем метод страницы - проверяем есть ли текст "login" в ссылке
    page.should_be_login_url()


def test_guest_should_see_login_form(browser):
    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page = LoginPage(browser, LoginPageLocators.LOGIN_PAGE_LINK)
    # открываем страницу
    page.open()
    # выполняем метод страницы - проверяем есть ли форма логина на странице
    page.should_be_login_form()


def test_guest_should_see_register_form(browser):
    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page = LoginPage(browser, LoginPageLocators.LOGIN_PAGE_LINK)
    # открываем страницу
    page.open()
    # выполняем метод страницы - проверяем есть ли форма регистрации на странице
    page.should_be_register_form()


if __name__ == '__main__':
    pytest.main()
