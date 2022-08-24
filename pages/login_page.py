from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from .base_page import BasePage
from .locators import LoginPageLocators



class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.is_current_link_true('login'), "Login link is not presented"

        #assert 'login' in self.current_url(), "Login link is not presented"
        #assert self.is_element_present(*LoginPageLocators.LOGIN_LINK), "Login link is not presented"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register link is not presented"

    def login(self, email, password):
        self.write_text_in_input(*LoginPageLocators.LOGIN_INPUT,email)
        self.write_text_in_input(*LoginPageLocators.PASSWORD_INPUT,email)
        log_in_btn = self.browser.find_element(*LoginPageLocators.LOG_IN_BTN)
        log_in_btn.click()

    def register_new_user(self, email, password):
        self.write_text_in_input(*LoginPageLocators.REG_LOG_INPUT, value=email)
        self.write_text_in_input(*LoginPageLocators.REG_PASS_INPUT,password)
        self.write_text_in_input(*LoginPageLocators.REG_CONF_PASS_INPUT,password)
        self.reg_btn = self.browser.find_element(*LoginPageLocators.REG_BTN)
        self.reg_btn.click()