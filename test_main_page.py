import time
from pages.main_page import MainPage # иногда в начале нужна точка

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    #page.go_to_login_page()          # выполняем метод страницы — переходим на страницу логина
    page.should_be_login_link()      # проверяем наличие ссылки на вход