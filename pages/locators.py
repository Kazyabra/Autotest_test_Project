# в файле локаторы
from selenium.webdriver.common.by import By


# локаторы главной страницы сайта
class MainPageLocators:
    MAIN_PAGE_LINK = 'http://selenium1py.pythonanywhere.com/'
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


# локаторы страницы авторизации
class LoginPageLocators:
    LOGIN_PAGE_LINK = 'http://selenium1py.pythonanywhere.com/en-gb/accounts/login/'
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
