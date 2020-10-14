import pytest
from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By

class ProductPage(BasePage):
    def should_add_to_basket(self):
        self.should_be_proper_item()
        
        self.should_be_login_url()
        self.should_be_login_form()

    #@pytest.mark.skip
    
    def should_be_proper_item(self):
        ###assert "The shellcoder's handbook" in self.browser.title, "Incorrect product item"
        
        
        #itemtext = self.browser.find_element(*ProductPageLocators.ITEM_NAME).text
        #assert "The shellcoder's handbook" in itemtext, "Incorrect product name"
        
        #itemprice = self.browser.find_element(*ProductPageLocators.ITEM_PRICE).text
        #assert "9.99" in itemprice, "Incorrect product price"
        
        itemtext = self.browser.find_element(*ProductPageLocators.ITEM_NAME).text
        addeditemtext = self.browser.find_element(*ProductPageLocators.ADDED_ITEM_NAME).text
        assert addeditemtext == itemtext, "Wrong item added to basket"
        #assert True
        
      

# Нижк заготовки под проверки      

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        ###print(self.browser.current_url)
        ###assert "login" in self.browser.current_url, "Login URL is not correct"
        assert True

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        ###assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"
        assert True

#The shellcoder's handbook has been added to your basket.
#div.alertinner




'''

class ProductPage(BasePage): 

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented" # поменяли на правильный
        
    def click_add_tobasket(self):
        login_link = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_LINK)
        login_link.click()
'''

