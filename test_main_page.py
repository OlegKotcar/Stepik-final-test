import time
from pages.main_page import MainPage # иногда в начале нужна точка
from pages.login_page import LoginPage # иногда в начале нужна точка

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/" #Рабочий линк
    
    #link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer" #линк с неверным локатором
    # Это из MainPage -----------------
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    
    page.go_to_login_page()          # выполняем метод страницы — переходим на страницу логина
    page.should_be_login_link()      # проверяем наличие ссылки на вход
    #------------------------------------
    # Это из LoginPage-----------------
    loginlink = "http://selenium1py.pythonanywhere.com/accounts/login/"
    loginpage = LoginPage(browser, loginlink)
    loginpage.open()
    loginpage.should_be_login_page()            # проверям наличи формы логин-регистрация