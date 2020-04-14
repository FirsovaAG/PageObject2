from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_ON_PAGE = (By.CSS_SELECTOR, ".btn-group .btn.btn-default")
    STUFF_IN_BASKET = (By.CSS_SELECTOR, ".basket-items .row")
    TEXT_ABOUT_EMPTY_BASKET = (By.CSS_SELECTOR, ".content_inner p")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    STUFF_IN_BASKET = (By.CSS_SELECTOR, ".basket-items .row")
    TEXT_ABOUT_EMPTY_BASKET = (By.CSS_SELECTOR, ".content_inner p")
    

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_PASSWORD1 = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_PASSWORD2 = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "#register_form .btn.btn-lg.btn-primary")
    EMAIL_TO_LOGIN = (By.CSS_SELECTOR, "#id_login-username")
    PASSWORD_TO_LOGIN = (By.CSS_SELECTOR, "#id_login-password")
    BUTTON_TO_LOGIN = (By.CSS_SELECTOR, "#login_form .btn.btn-lg.btn-primary")
    
class ProductPageLocators():
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-lg.btn-primary.btn-add-to-basket")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert.alert-safe.alert-noicon.alert-success.fade.in")
    BASKET_ON_PRODUCT_PAGE = (By.CSS_SELECTOR, ".btn.btn-default")
    PRICE_OF_PRODUCT = (By.CSS_SELECTOR, ".col-sm-6.product_main .price_color")
    PRICE_IN_MESSAGE_ADD_BASKET =(By.CSS_SELECTOR, ".alert.alert-safe.alert-noicon.alert-info.fade.in .alertinner strong")
    NAME_OF_PRODUCT = (By.CSS_SELECTOR, ".col-sm-6.product_main h1")
    PRODUCT_IN_MESSAGE_ADD_BASKET =(By.CSS_SELECTOR, ".alert.alert-safe.alert-noicon.alert-success.fade.in .alertinner strong")

