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
        assert self.is_text_in_url(LoginPageLocators.LOGIN_URL), 'login url not correct'

    def should_be_login_form(self):
        # проверка, что есть форма логина
        self.is_element_present(*LoginPageLocators.LOGIN_FORM)

    def should_be_register_form(self):
        # проверка, что есть форма регистрации на странице
        self.is_element_present(*LoginPageLocators.REGISTRATION_FORM)

    def register_new_user(self, email, password):
        # выводим email, password
        print(f'email: {email}  password: {password}')
        self.send_reg_email(email)
        print(f'внесена информация в поле email')
        self.send_reg_password(password)
        print(f'внесена информация в поле password')
        self.send_reg_confirm(password)
        print(f'внесена информация в поле confirm')
        self.button_reg_confirm_click()
        print(f'нажата кнопка Register')

    def should_be_input_reg_email(self):
        # проверка, что есть поле email форме регистрации на странице
        self.is_element_present(*LoginPageLocators.INPUT_REG_EMAIL)

    def should_be_input_reg_pass(self):
        # проверка, что есть поле password в форме регистрации на странице
        self.is_element_present(*LoginPageLocators.INPUT_REG_PASS)

    def should_be_input_reg_confirm(self):
        # проверка, что есть поле confirm password в форме регистрации на странице
        self.is_element_present(*LoginPageLocators.INPUT_REG_CONFIRM)

    def send_reg_email(self, email):
        # вписать email
        self.try_send_keys(*LoginPageLocators.INPUT_REG_EMAIL, email)

    def send_reg_password(self, password):
        # вписать пароль
        self.try_send_keys(*LoginPageLocators.INPUT_REG_PASS, password)

    def send_reg_confirm(self, password):
        # вписать подтверждение пароля
        self.try_send_keys(*LoginPageLocators.INPUT_REG_CONFIRM, password)

    def button_reg_confirm_click(self):
        # кликнуть кнопку подтверждения регистрации
        self.is_element_click(*LoginPageLocators.REG_BUTTON)
