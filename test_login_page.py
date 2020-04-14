from .pages.login_page import LoginPage
import time
import pytest

def test_guest_should_see_login_form(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    page = LoginPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    time.sleep(10)
    page.should_be_login_page()
    

def test_regster_new_user(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.register_for_guest()
    time.sleep(10)
    page.should_be_authorized_user()
    
