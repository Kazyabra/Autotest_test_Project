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
    LOGIN_URL = 'login'


# локаторы страницы product_page
class ProductPageLocators:
    PRODUCT_PAGE_LINK = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/' \
                        '?promo=newYear'
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main>h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main>p.price_color')
    BTN_ADD_TO_BASKET = (By.CSS_SELECTOR, '#add_to_basket_form > button')
    PROMO_URL = '?promo=newYear'
    MESSAGE_ADD_NAME = (By.CSS_SELECTOR, '#messages > div:nth-child(1) >.alertinner strong')
    MESSAGE_ADD_PRICE = (By.CSS_SELECTOR, '#messages > div:nth-child(3) >.alertinner strong')
