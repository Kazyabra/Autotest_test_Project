# в файле локаторы

from selenium.webdriver.common.by import By


# базовые локаторы
class BasePageLocators:
    BASKET_BUTTON = (By.CSS_SELECTOR, '.btn-group>a')
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


# локаторы главной страницы сайта
class MainPageLocators:
    MAIN_PAGE_LINK = 'http://selenium1py.pythonanywhere.com/'


# локаторы страницы авторизации
class LoginPageLocators:
    LOGIN_PAGE_LINK = 'http://selenium1py.pythonanywhere.com/accounts/login/'
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
    LOGIN_URL = 'login'
    INPUT_REG_EMAIL = (By.CSS_SELECTOR, "#register_form input[type='email'")
    INPUT_REG_PASS = (By.CSS_SELECTOR, "#register_form input[name='registration-password1']")
    INPUT_REG_CONFIRM = (By.CSS_SELECTOR, "#register_form input[name='registration-password2']")
    REG_BUTTON = (By.CSS_SELECTOR, "#register_form .btn-lg")


# локаторы страницы product_page
class ProductPageLocators:
    PRODUCT_PAGE_LINK = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main>h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main>p.price_color')
    BTN_ADD_TO_BASKET = (By.CSS_SELECTOR, '#add_to_basket_form > button')
    PROMO_URL = '?promo=newYear'
    MESSAGE_ADD_NAME = (By.CSS_SELECTOR, '#messages > div:nth-child(1) >.alertinner strong')
    MESSAGE_ADD_PRICE = (By.CSS_SELECTOR, '#messages > div:nth-child(3) >.alertinner strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '#messages>.alert')


# Локаторы страницы корзина
class BasketPageLocators:
    BASKET_EMPTY_MESSAGE = (By.CSS_SELECTOR, '#content_inner>p')
    ORDER_TOTAL_PRICE = (By.CSS_SELECTOR, '#basket_totals h3.price_color')
