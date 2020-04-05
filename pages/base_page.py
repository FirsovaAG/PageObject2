from selenium.common.exceptions import NoSuchElementException

class BasePage():

    def __init__(self, browser, url, timeout=10):
        #Внутри конструктора сохраняем эти данные как аттрибуты нашего класса
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        #добавим еще один метод, который открывает нужную страницу в браузере
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True
