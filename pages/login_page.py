from .base_page import BasePage
from .locators import LoginPageLocators
import time


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.url.find("login") > 0, "Link of login_page is not corrected"
        # реализация проверки url

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not found"
        #проверка, что есть форма логина

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not found"
        #проверка, что есть форма регистрации на странице

    def register_for_guest(self):
        input_registre_email = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL)
        input_registre_email.send_keys(f"{time.time()}@gmail.com")
        input_registre_password1 = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD1)
        input_registre_password1.send_keys("sonfgys19")
        input_registre_password2 = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD2)
        input_registre_password2.send_keys("sonfgys19")
        button_registre = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        button_registre.click()

    def register_user(self, email, password):
        email_field = self.browser.find_element(*LoginPageLocators.EMAIL_TO_LOGIN)
        email_field.send_keys(email)
        password_field = self.browser.find_element(*LoginPageLocators.PASSWORD_TO_LOGIN)
        password_field.send_keys(password)
        button_to_login = self.browser.find_element(*LoginPageLocators.BUTTON_TO_LOGIN)
        button_to_login.click()

    def register_new_user(self, email, password):
        email_field = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL)
        email_field.send_keys(email)
        password1_field = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD1)
        password1_field.send_keys(password)
        password2_field = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD2)
        password2_field.send_keys(password)
        button_to_register = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        button_to_register.click()        
    


        
        
        
        
        
        
