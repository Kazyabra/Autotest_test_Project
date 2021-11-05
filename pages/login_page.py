from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        # все проверки на странице
        errors = ''
        try:
            self.should_be_login_url()
        except:
            errors = 'Test should_be_login_url FAILED\n'
        try:
            self.should_be_login_form()
        except:
            errors += 'Test should_be_login_form FAILED\n'
        try:
            self.should_be_register_form()
        except:
            errors += 'Test should_be_register_form FAILED'
        finally:
            assert not errors, errors

    def should_be_login_url(self):
        # проверка на корректный url адрес
        assert self.is_text_in_url('login'), 'login url not correct'

    def should_be_login_form(self):
        # проверка, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), 'login form not presented'

    def should_be_register_form(self):
        # проверка, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), 'registration form not presented'
