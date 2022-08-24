from .locators import BasketPageLocators
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException # в начале файла
from selenium.common.exceptions import TimeoutException
from .base_page import BasePage


class BasketPage(BasePage):
    def check_empty_basket(self):
        basket_should_be_empty_positive()
        basket_should_be_empty_negative()

    def basket_should_be_empty_positive(self):
        assert self.is_element_present(*BasketPageLocators.ITEMS_DIV) == False, "Basket is not empty"

    def basket_should_be_empty_negative(self):
        assert self.is_element_present(*BasketPageLocators.ITEMS_DIV) == True, "Basket is empty"
