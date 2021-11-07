import math
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import BasePageLocators


class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def go_to_basket_page(self):
        # пробует кликнуть кнопку с корзиной
        # символ * указывает на то, что мы передали пару, и этот кортеж нужно распаковать
        assert self.is_element_click(*BasePageLocators.BASKET_BUTTON), 'failed to follow the basket page'
        print('Нажата кнопка перехода в корзину')

    def go_to_login_page(self):
        # пробует кликнуть ссылку страницы с логином
        # символ * указывает на то, что мы передали пару, и этот кортеж нужно распаковать
        assert self.is_element_click(*BasePageLocators.LOGIN_LINK), 'failed to follow the login link'

    def should_be_login_link(self):
        # пробует найти ссылку страницы с логином
        # символ * указывает на то, что мы передали пару, и этот кортеж нужно распаковать
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), 'Login link is not presented'

    def is_element_present(self, how, what):
        # проверка элемента на наличие
        try:
            element = self.browser.find_element(how, what)
            print(f'Элемент {what} найден')
        except NoSuchElementException:
            print(f'Элемент {what} не найден')
            return False
        # если элемент найден, то возвращает его
        return element

    def is_element_click(self, how, what):
        # проверка элемента на клик
        try:
            element = self.is_element_present(how, what)
            element.click()
            print(f'Элемент {what} кликнут мышкой')
        except:
            print(f'Элемент {what} не удалось кликнуть мышкой')
            return False
        return element

    def is_not_element_present(self, how, what, timeout=4):
        # проверяет, что элемент не появляется на странице в течении 4 сек
        # если не появился, то True
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            print(f'Успех: Ждали появления элемента {what} {timeout} секунды. Элемент не появился.')
            return True
        print(f'Неудача: Ждали появления элемента {what} {timeout} секунды. Элемент появился.')
        return False

    def is_disappeared(self, how, what, timeout=4):
        # проверяет, что элемент пропадает со страницы в течении 4 сек
        # если пропадает, то True
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).\
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            print(f'Неудача: Ждали, что элемент {what} пропадет {timeout} секунды. Элемент не пропал.')
            return False
        print(f'Успех: Ждали, что элемент {what} пропадет {timeout} секунды. Элемент пропал.')
        return True

    def is_text_in_url(self, text):
        # получаем текущий url страницы
        url = self.browser.current_url
        if text in url:
            print(f'"{text}" присутствует в ссылке {url}')
            return True
        else:
            print(f'"{text}" отсутствует в ссылке {url}')
            return False

    def open(self):
        # открыть ссылку в браузере
        try:
            self.browser.get(self.url)
            print(f'\nСсылка {self.url} открыта')
        except:
            print(f'\nНе смог открыть ссылку {self.url}')
            return False
        return True

    def solve_quiz_and_get_code(self):
        # получение кодов для прохождения тестовых заданий
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        print('Данные для вычислений получены')
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        print('Ответ отправлен')
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")


if __name__ == '__main__':
    pass
