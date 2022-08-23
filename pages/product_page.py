from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def check_add_product(self):
#        self.should_be_promo_in_link()
        self.add_product_to_basket()
        self.solve_quiz_and_get_code()
        self.check_price_basket()
        self.check_added_product_by_name()

#    def should_be_promo_in_link(self):
#        assert self.is_current_link_true('promo=offer'), "Promo in link is not presented"
    def add_product_to_basket(self):
        btn_add_to_basket = self.browser.find_element(*ProductPageLocators.BTN_ADD_TO_BASKET)
        btn_add_to_basket.click()
        
    def check_price_basket(self):
        product_price = self.get_text_in_element(*ProductPageLocators.PRODUCT_PRICE)
        basket_price = self.get_text_in_element(*ProductPageLocators.BASKET_PRICE)
        assert product_price in basket_price, 'Price product != price in basket'

    def check_added_product_by_name(self):
        product_name = self.get_text_in_element(*ProductPageLocators.PRODUCT_NAME)
        alert_product_name = self.get_text_in_element(*ProductPageLocators.ALERT_PRODUCT_NAME)
        assert product_name == alert_product_name, 'To basket added another product by name'


