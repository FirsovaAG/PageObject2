

class BasePage():

    def __init__(self, browser, url):
        #Внутри конструктора сохраняем эти данные как аттрибуты нашего класса
        self.browser = browser
        self.url = url

    def open(self):
        #добавим еще один метод, который открывает нужную страницу в браузере
        self.browser.get(self.url)
