from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, 'div .basket-mini > span > a')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    ITEMS_DIV = (By.CSS_SELECTOR, 'div .basket-items')

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
    LOGIN_INPUT = (By.CSS_SELECTOR, '#id_login-username')
    PASSWORD_INPUT = (By.CSS_SELECTOR, 'id_login-password')
    LOG_IN_BTN = (By.XPATH, '//button[@name="login_submit"]')
    LOGIN_INPUT = (By.CSS_SELECTOR, '#id_login-username')
    PASSWORD_INPUT = (By.CSS_SELECTOR, 'id_login-password')
    LOG_IN_BTN = (By.XPATH, '//button[@name="login_submit"]')
    REG_LOG_INPUT = (By.CSS_SELECTOR, '#id_registration-email')
    REG_PASS_INPUT = (By.CSS_SELECTOR, '#id_registration-password1')
    REG_CONF_PASS_INPUT = (By.CSS_SELECTOR, '#id_registration-password2')
    REG_BTN = (By.XPATH, '//button[@name="registration_submit"]')


class ProductPageLocators():
    BTN_ADD_TO_BASKET = (By.CSS_SELECTOR, '.btn-add-to-basket')
    PRODUCT_PRICE = (By.CSS_SELECTOR, 'div .product_main > p.price_color')
    BASKET_PRICE = (By.CSS_SELECTOR, 'div .basket-mini.pull-right.hidden-xs')
    PRODUCT_NAME = (By.CSS_SELECTOR, '#content_inner h1')
    ALERT_PRODUCT_NAME = (By.CSS_SELECTOR, '.alertinner > strong')