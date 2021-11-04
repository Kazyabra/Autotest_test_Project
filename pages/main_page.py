from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import MainPageLocators


class MainPage(BasePage):

    def go_to_login_page(self):
        # символ * указывает на то, что мы передали пару, и этот кортеж нужно распаковать
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()

    def should_be_login_link(self):
        # символ * указывает на то, что мы передали пару, и этот кортеж нужно распаковать
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), 'Login link is not presented'


if __name__ == '__main__':
    pass
