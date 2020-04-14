from .base_page import BasePage
from .locators import ProductPageLocators
import time

class ProductPage(BasePage):
    def should_be_product_page(self):
        self.should_be_button_add_to_basket()
        self.should_be_basket_on_product_page()

    def should_be_button_add_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.BUTTON_ADD_TO_BASKET), "Button to add basket is not found"
        #проверка, что есть кнопка "Добавить в корзину"

    def should_be_basket_on_product_page(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_ON_PRODUCT_PAGE), "Basket on product's page to add basket is not found"
        #проверка, что есть кнопка "Корзина" на странице товара

    def add_product_to_basket(self):
        button_add_to_basket = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        button_add_to_basket.click()
        #добавление товара в корзину

    def add_product_to_basket_promo(self):
        button_add_to_basket = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        button_add_to_basket.click()
        self.solve_quiz_and_get_code()
        #добавление товара в корзину с вычислением значения для промоакций
        
    def should_be_correct_price_on_basket(self):
        price_of_product = self.browser.find_element(*ProductPageLocators.PRICE_OF_PRODUCT).text
        price_on_addmessage = self.browser.find_element(*ProductPageLocators.PRICE_IN_MESSAGE_ADD_BASKET).text
        assert price_on_addmessage == price_of_product, "Price of product in message about add don't coincaid with name of product"
        #проверка соответсвия цены товара в сообщении о добавлении в корзину

    def should_be_correct_name_on_basket(self):
        name_of_product = self.browser.find_element(*ProductPageLocators.NAME_OF_PRODUCT).text
        name_product_on_addmessage = self.browser.find_element(*ProductPageLocators.PRODUCT_IN_MESSAGE_ADD_BASKET).text
        assert name_of_product == name_product_on_addmessage, "Name of product in message about add don't coincaid with name of product"
        #проверка соответствия наименования товара в сообщении о добавлении в корзину

    def not_message_is_not_element_present(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE),\
               "Success message is presented"
        #сообщение о добавлении присутсвует
        
    def not_message_is_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE),\
               "Success message is not presented"
        #сообщение о добавлении отсутсвует

