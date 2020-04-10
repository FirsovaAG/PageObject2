from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    
class ProductPageLocators():
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-lg.btn-primary.btn-add-to-basket")
    BASKET_ON_PRODUCT_PAGE = (By.CSS_SELECTOR, ".btn.btn-default")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert.alert-safe.alert-noicon.alert-success.fade.in")
    PRICE_OF_PRODUCT = (By.CSS_SELECTOR, ".col-sm-6.product_main .price_color")
    PRICE_IN_MESSAGE_ADD_BASKET =(By.CSS_SELECTOR, ".alert.alert-safe.alert-noicon.alert-info.fade.in .alertinner strong")
    NAME_OF_PRODUCT = (By.CSS_SELECTOR, ".col-sm-6.product_main h1")
    PRODUCT_IN_MESSAGE_ADD_BASKET =(By.CSS_SELECTOR, ".alert.alert-safe.alert-noicon.alert-success.fade.in .alertinner strong")

