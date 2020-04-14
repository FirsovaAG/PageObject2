from .base_page import BasePage
from .locators import BasketPageLocators
import time

class BasketPage(BasePage):
    def should_not_be_product_in_a_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.STUFF_IN_BASKET), "Product is presented in basket"

        
    def should_be_text_about_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.TEXT_ABOUT_EMPTY_BASKET), "Text about empty basket is not presented in basket"
        "Success message is not presented"
        #сообщение о добавлении отсутсвует

    def should_be_product_in_a_basket(self):
        assert self.is_element_present(BasketPageLocators.STUFF_IN_BASKET), "Product is not presented in basket"
        

    def should_not_be_text_about_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.TEXT_ABOUT_EMPTY_BASKET), "Text about empty basket is not presented in basket"
        "Success message is presented"
        


