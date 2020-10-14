import pytest
from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By

class ProductPage(BasePage):
    def should_add_to_basket(self):
        self.should_be_proper_item()
        
        
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

    def should_not_be_success_message(self):
        
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"
        #assert True 

    def should_success_message_diasppeared(self):
        
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is not disappeared, but should be"
        #assert True 
 
 
 
      

