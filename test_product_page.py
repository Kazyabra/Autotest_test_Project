# pytest -v --tb=line --language=en test_product_page.py
# pytest -s --language=en test_product_page.py

import pytest
from .pages.locators import ProductPageLocators
from .pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(browser):
    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page = ProductPage(browser, ProductPageLocators.PRODUCT_PAGE_LINK)
    # открываем страницу
    page.open()
    # выполняем метод страницы - проверяем добавление в корзину
    page.product_promo_page_add_to_basket()


if __name__ == '__main__':
    pytest.main()
# Ответ 27.258251974806797
