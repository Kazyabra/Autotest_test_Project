import pytest
from .base_page import BasePage
from .locators import MainPageLocators


class MainPage(BasePage):

    def go_to_login_page(self):
        # пробует кликнуть ссылку страницы с логином
        # символ * указывает на то, что мы передали пару, и этот кортеж нужно распаковать
        assert self.is_element_click(*MainPageLocators.LOGIN_LINK), 'failed to follow the login link'

    def should_be_login_link(self):
        # пробует найти ссылку страницы с логином
        # символ * указывает на то, что мы передали пару, и этот кортеж нужно распаковать
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), 'Login link is not presented'


if __name__ == '__main__':
    pytest.main()
