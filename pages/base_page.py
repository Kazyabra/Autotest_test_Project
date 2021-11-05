from selenium.common.exceptions import NoSuchElementException


class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        # открыть ссылку в браузере
        try:
            self.browser.get(self.url)
            print(f'\nСсылка {self.url} открыта')
        except:
            print(f'\nне смог открыть ссылку {self.url}')
            return False
        return True

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
            self.is_element_present(how, what).click()
            print(f'элемент {what} кликнут мышкой')
        except:
            print(f'элемент {what} не удалось кликнуть мышкой')
            return False
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


if __name__ == '__main__':
    pass
