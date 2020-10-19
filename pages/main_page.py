#импорт из подкаталога pages где-то работает с "." где-то нет
from .base_page import BasePage
from .locators import MainPageLocators
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By
from .login_page import LoginPage


class MainPage(BasePage): 
    #Поставили заглушку, т.к. все вынесли в BasePage и locators
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)
        
    #Можно еще короче
    # class MainPage(BasePage):
    #pass    
        
    
        
class MainProductPage(BasePage): 
        
    def should_be_add_to_basket_link(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), "Add to cart link is not presented"
    
    def click_add_to_basket(self):
        AddButton = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        AddButton.click()
    
