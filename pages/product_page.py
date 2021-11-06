from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def product_promo_page_add_to_basket(self):
        # метод проверяет добавление товара в корзину(с задачкой)
        self.should_be_login_url()
        # запоминаем цену и наименование товара
        name = self.should_be_product_name().text
        price = self.should_be_product_price().text
        # добавляем товар в корзину
        self.btn_add_to_basket_click()
        # смотрим и считаем матем. выраж, отправляем ответ и получаем код
        self.solve_quiz_and_get_code()
        # смотрим что добавилось в корзину
        add_name = self.should_be_message_add_name().text
        add_price = self.should_be_message_add_price().text
        # сверяем цену и наименование с тем что упало в корзину
        assert name == add_name, 'Наименование товара не совпадает'
        print('Наименование товара совпадает')
        assert price == add_price, 'Цена товара не совпадает'
        print('Цена товара совпадает')

    def should_be_login_url(self):
        # проверка на корректный url адрес
        assert self.is_text_in_url(ProductPageLocators.PROMO_URL), 'promo url not correct'

    def should_be_product_name(self):
        # проверка, что есть элемент
        product_name = self.is_element_present(*ProductPageLocators.PRODUCT_NAME)
        assert product_name, 'element PRODUCT_NAME not found'
        return product_name

    def should_be_product_price(self):
        # проверка, что есть элемент
        product_price = self.is_element_present(*ProductPageLocators.PRODUCT_PRICE)
        assert product_price, 'element PRODUCT_PRICE not found'
        return product_price

    def should_be_btn_add_to_basket(self):
        # проверка, что есть элемент
        btn_add_to_basket = self.is_element_present(*ProductPageLocators.BTN_ADD_TO_BASKET)
        assert btn_add_to_basket, 'element BTN_ADD_TO_BASKET not found'
        return btn_add_to_basket

    def btn_add_to_basket_click(self):
        # пробует кликнуть кнопку Добавить в корзину
        btn_add_to_basket = self.is_element_click(*ProductPageLocators.BTN_ADD_TO_BASKET)
        assert btn_add_to_basket, 'failed to click button BTN_ADD_TO_BASKET'
        return btn_add_to_basket

    def should_be_message_add_name(self):
        # проверка, что есть элемент
        message_add_name = self.is_element_present(*ProductPageLocators.MESSAGE_ADD_NAME)
        assert message_add_name, 'element MESSAGE_ADD_NAME not found'
        return message_add_name

    def should_be_message_add_price(self):
        # проверка, что есть элемент
        message_add_price = self.is_element_present(*ProductPageLocators.MESSAGE_ADD_PRICE)
        assert message_add_price, 'element MESSAGE_ADD_PRICE not found'
        return message_add_price


if __name__ == '__main__':
    pass
