import time, pytest
#from pages.main_page import MainPage # иногда в начале нужна точка
from pages.main_page import MainProductPage
from pages.product_page import ProductPage # иногда в начале нужна точка

'''
def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/" #Рабочий линк
    
    #link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer" #линк с неверным локатором
    # Это из MainPage -----------------
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    
    #page.go_to_login_page()          # выполняем метод страницы — переходим на страницу логина
    #page.should_be_login_link()      # проверяем наличие ссылки на вход
    
    #------------------------------------
    # Это из LoginPage-----------------
    loginlink = browser.current_url
    
    loginpage = LoginPage(browser, loginlink)
    #loginpage.open()
    loginpage.should_be_login_page()            # проверям наличи формы логин-регистрация
'''



@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])




#!!!!!!!!!!
#product_base_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
####urls = [f"{product_base_link}/?promo=offer{no}" for no in range(10)]


                               
#@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7"])
#7 - с ошибкой
    
def test_guest_can_add_product_to_basket(browser, link):
#def test_guest_can_add_product_to_basket(browser):
    
    #browser.delete_all_cookies()  # очистка кукисов
    
    
    #link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    
    #link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    
    
    mainproductpage = MainProductPage(browser, link)
    mainproductpage.open()
    mainproductpage.should_be_add_to_basket_link()
    mainproductpage.click_add_to_basket()
    mainproductpage.solve_quiz_and_get_code()  # Нужен алерт для этого метода
    #time.sleep(25)
    
    
    itempage = ProductPage(browser, browser.current_url)
    itempage.should_add_to_basket()
    
    
    
    
    


# -----------

