#импорт из подкаталога pages где-то работает с "." где-то нет
from .base_page import BasePage
from .locators import MainPageLocators
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By
from .login_page import LoginPage


class MainPage(BasePage): 
    '''
    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()
        
        # Массовая обработка алертов на страницах если надо
        ##alert = self.browser.switch_to.alert
        ##alert.accept()
        
        #return LoginPage(browser=self.browser, url=self.browser.current_url)
        
    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented" # поменяли на правильный
    '''
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
    
