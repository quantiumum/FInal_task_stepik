from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from .pages.product_page import ProductPage
import pytest
    
@pytest.mark.sample
def test_guest_can_add_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.check_add_product()


def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, timeout=0):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.check_guest_cant_see_success_message_after_adding_product_to_basket()

def test_guest_cant_see_success_message(browser, timeout=0):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.check_guest_cant_see_success_message()

def test_message_disappeared_after_adding_product_to_basket(browser, timeout=0):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.check_message_disappeared_after_adding_product_to_basket()