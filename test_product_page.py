# pytest -v --tb=line --language=en test_product_page.py
# pytest -s --language=en test_product_page.py

import pytest
from .pages.locators import ProductPageLocators
from .pages.product_page import ProductPage

# добавляем параметризацию 10 промоссылок
promolink = [(lambda i: '?promo=offer'+str(i))(i) for i in range(0, 10)]
# помечаем промо7, как xfail
promolink[7] = pytest.param(promolink[7], marks=pytest.mark.xfail)


@pytest.mark.parametrize('promo', promolink)  # параметризация
def test_guest_can_add_product_to_basket(browser, promo):
    ProductPageLocators.PROMO_URL = promo  # меняем обычный промо на новый
    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page = ProductPage(browser, ProductPageLocators.PRODUCT_PAGE_LINK + promo)
    # открываем страницу
    page.open()
    # выполняем метод страницы - проверяем добавление в корзину
    page.product_promo_page_add_to_basket()


if __name__ == '__main__':
    pytest.main()
