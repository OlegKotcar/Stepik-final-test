import time, pytest
from .base_page import BasePage
from .locators import BasePageLocators



class BasketPage(BasePage):
   
    def should_be_no_items_in_basket(self):
       
        EmptyBasketText = self.browser.find_element(*BasePageLocators.EMPTY_BASKET_TAG).text
        assert "Your basket is empty" in EmptyBasketText, "Basket is not empty"
        assert self.is_not_element_present(*BasePageLocators.NOT_EMPTY_BASKET_TAG), "Not empty Basket tag present" 


'''
    def should_not_be_success_message(self):
        
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"
        #assert True 

    def should_success_message_diasppeared(self):
        
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is not disappeared, but should be"
        #assert True 
 
 
 
      

'''

#-------