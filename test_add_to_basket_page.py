import time
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

    
def test_guest_can_add_product_to_basket(browser):
    #link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    
    
    mainproductpage = MainProductPage(browser, link)
    mainproductpage.open()
    mainproductpage.should_be_add_to_basket_link()
    mainproductpage.click_add_to_basket()
    mainproductpage.solve_quiz_and_get_code()  # Нужен алерт для этого метода
    #time.sleep(5)
    
    
    itempage = ProductPage(browser, browser.current_url)
    itempage.should_add_to_basket()
    
    


# -----------

