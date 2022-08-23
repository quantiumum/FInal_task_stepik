from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
    
class ProductPageLocators():
    BTN_ADD_TO_BASKET = (By.CSS_SELECTOR, '.btn-add-to-basket')
    PRODUCT_PRICE = (By.CSS_SELECTOR, 'div .product_main > p.price_color')
    BASKET_PRICE = (By.CSS_SELECTOR, 'div .basket-mini.pull-right.hidden-xs')
    PRODUCT_NAME = (By.CSS_SELECTOR, '#content_inner h1')
    ALERT_PRODUCT_NAME = (By.CSS_SELECTOR, '.alertinner > strong')