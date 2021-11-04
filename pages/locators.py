# в файле локаторы
from selenium.webdriver.common.by import By


# локаторы главной страницы сайта
class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


# локаторы страницы авторизации
class LoginPageLocators:

