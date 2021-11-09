# варианты запуска
# pytest -v --tb=line --language=en test_product_page.py
# pytest -s --language=en test_product_page.py
# pytest -s --language=en -m user_add_to_basket test_product_page.py

import pytest
import time
from .pages.locators import ProductPageLocators, LoginPageLocators
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage

# добавляем параметризацию 10 промоссылок
promolink = [(lambda i: '?promo=offer' + str(i))(i) for i in range(0, 10)]
# помечаем промо7, как xfail
promolink[7] = pytest.param(promolink[7], marks=pytest.mark.xfail)


@pytest.mark.skip(reason="Тест пропущен")
@pytest.mark.parametrize('promo', promolink)  # параметризация
def test_guest_can_add_product_to_basket(browser, promo):
    ProductPageLocators.PROMO_URL = promo  # меняем обычный промо на новый
    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page = ProductPage(browser, ProductPageLocators.PRODUCT_PAGE_LINK + promo)
    # открываем страницу
    page.open()
    # выполняем метод страницы - проверяем добавление в корзину
    page.product_promo_page_add_to_basket()


@pytest.mark.xfail(reason="Тест ожидаемо падает")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    """
    быть неавторизованным
    1. открыть страницу с товаром
    2. ткнуть кнопку добавить
    3. проверить, что нет сообщения об успехе с помощью is_not_element_present
    """
    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page = ProductPage(browser, ProductPageLocators.PRODUCT_PAGE_LINK)
    # открываем страницу
    page.open()
    # кликает кнопку
    page.btn_add_to_basket_click()
    # ставит ожидание в 1сек
    page.browser.implicitly_wait(1)
    # проверяет, что нет сообщения о добавлении в корзину
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    """
    быть неавторизованным
    1. открыть страницу с товаром
    2. проверить, что нет сообщения об успехе с помощью is_not_element_present
    """
    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page = ProductPage(browser, ProductPageLocators.PRODUCT_PAGE_LINK)
    # открываем страницу
    page.open()
    # ставит ожидание в 1сек
    page.browser.implicitly_wait(1)
    # проверяет, что нет сообщения о добавлении в корзину
    page.should_not_be_success_message()


@pytest.mark.xfail(reason="Тест ожидаемо падает")
def test_message_disappeared_after_adding_product_to_basket(browser):
    """
    быть неавторизованным
    1. открыть страницу с товаром
    2. ткнуть кнопку добавить
    3. Проверяем, что пропадет сообщения об успехе с помощью is_disappeared
    """
    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page = ProductPage(browser, ProductPageLocators.PRODUCT_PAGE_LINK)
    # открываем страницу
    page.open()
    # кликает кнопку
    page.btn_add_to_basket_click()
    # ставит ожидание в 1сек
    page.browser.implicitly_wait(1)
    # проверяет, что сообщение о добавлении пропало
    page.success_message_is_disappeared()


def test_guest_should_see_login_link_on_product_page(browser):
    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page = ProductPage(browser, ProductPageLocators.PRODUCT_PAGE_LINK)
    # открываем страницу
    page.open()
    # выполняем метод страницы - ищем ссылку на страницу логина
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page = ProductPage(browser, ProductPageLocators.PRODUCT_PAGE_LINK)
    # открываем страницу
    page.open()
    # выполняем метод страницы - переходим на страницу логина
    page.go_to_login_page()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    """
    1. Гость открывает страницу товара
    2. Переходит в корзину по кнопке в шапке
    3. Ожидаем, что в корзине нет товаров
    4. Ожидаем, что есть текст о том что корзина пуста
    """
    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page = ProductPage(browser, ProductPageLocators.PRODUCT_PAGE_LINK)
    # [1] открываем страницу
    page.open()
    # [2] выполняем метод страницы base page - переходим на страницу корзины
    page.go_to_basket_page()
    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и текущий url адрес
    page = BasketPage(browser, browser.current_url)
    # [3] проверяем, что в корзине нет товаров
    # ставит ожидание в 1сек
    page.browser.implicitly_wait(1)
    page.should_not_be_order_total_price()
    # ставит ожидание в 10сек
    page.browser.implicitly_wait(10)
    # [4] проверяем, что есть текст, о том, что корзина пуста
    page.should_be_message_basket_empty()

@pytest.mark.user_add_to_basket
class TestUserAddToBasketFromProductPage:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        """
        предустановка для тестов этого класса
        запускается перед каждым тестом
        регистрирует нового пользователя
        """
        # открываем страницу регистрации
        page = LoginPage(browser, LoginPageLocators.LOGIN_PAGE_LINK)
        page.open()
        # регистрируем нового пользователя
        email = f'SP{str(time.time())}@fakemail.org'  # генерируем адрес почты
        password = '789QwertY123'
        page.register_new_user(email, password)
        # проверяем, что пользователь зарегистрирован
        page.should_be_authorized_user()
        print(f'Успех: регистрация нового пользователя проведена')

    def test_user_cant_see_success_message(self, browser):
        """
        быть авторизованным
        1. открыть страницу с товаром
        2. проверить, что нет сообщения об успехе с помощью is_not_element_present
        """
        # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page = ProductPage(browser, ProductPageLocators.PRODUCT_PAGE_LINK)
        # открываем страницу
        page.open()
        # ставит ожидание в 1сек
        page.browser.implicitly_wait(1)
        # проверяет, что нет сообщения о добавлении в корзину
        page.should_not_be_success_message()

    def test_user_can_add_product_to_basket(self, browser):
        # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page = ProductPage(browser, ProductPageLocators.PRODUCT_PAGE_LINK)
        # открываем страницу
        page.open()
        # выполняем метод страницы - проверяем добавление в корзину
        page.product_page_add_to_basket()


if __name__ == '__main__':
    pytest.main()
