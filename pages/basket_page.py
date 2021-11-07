# Страница корзины
from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def should_not_be_order_total_price(self):
        # проверяет, что ORDER_TOTAL_PRICE отсутствует на странице
        assert self.is_not_element_present(*BasketPageLocators.ORDER_TOTAL_PRICE), \
            "ORDER_TOTAL_PRICE есть, а его быть не должно"
        print('Успех: Итоговой цены корзины нет')

    def should_be_message_basket_empty(self):
        # проверка, что есть элемент
        message_basket_empty = self.is_element_present(*BasketPageLocators.BASKET_EMPTY_MESSAGE)
        assert message_basket_empty, 'element BASKET_EMPTY_MESSAGE not found'
        print('Есть сообщение, что корзина пуста')
        return message_basket_empty


if __name__ == '__main__':
    pass
