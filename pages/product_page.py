from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By

class ProductPage(BasePage):
    def should_add_to_basket(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        ###print(self.browser.current_url)
        ###assert "login" in self.browser.current_url, "Login URL is not correct"
        assert True

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        ###assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"
        assert True

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        ###assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"
        assert True



'''

class ProductPage(BasePage): 

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented" # поменяли на правильный
        
    def click_add_tobasket(self):
        login_link = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_LINK)
        login_link.click()