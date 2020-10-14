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




@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
 # Это линк с ошибкой - пометили как XFail                                 "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                  pytest.param("bugged_link", marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])

# Помечаем XFail в параметризации
#@pytest.mark.parametrize('link', ["okay_link",
#                                  pytest.param("bugged_link", marks=pytest.mark.xfail),
#                                  "okay_link"])


'''



#product_base_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
####urls = [f"{product_base_link}/?promo=offer{no}" for no in range(10)]


@pytest.mark.skip                              
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1"])
#7 - с ошибкой
    
def test_guest_can_add_product_to_basket(browser, link):
#def test_guest_can_add_product_to_basket(browser):
    
    #browser.delete_all_cookies()  # очистка кукисов
       
    #link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    #link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    
    
    mainproductpage = MainProductPage(browser, link)
    itempage = ProductPage(browser, browser.current_url)
    
    mainproductpage.open()  #Открываем страницу товара
    itempage.should_not_be_success_message() # проверяем что нет сообщения о добавлении в корзину(мы только вошли на страницу) 4 сек. ожидание по-умолчанию
    
    
    mainproductpage.should_be_add_to_basket_link() # Есть кнопка добавить в корзину
    
    mainproductpage.click_add_to_basket() #Наживаем добавить в корзину
    mainproductpage.solve_quiz_and_get_code()  # Нужен алерт для этого метода - решаем, вставляем значение 
    time.sleep(5)
        
    
    itempage.should_be_proper_item() # проверяем что в корзину добавлен правильный товар
    
    #itempage.should_not_be_success_message() #Упадет с ошибкой т.к. товар добавлен и SUCCESS_MESSAGE есть на странице
  

@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"])
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, link):    
   
    
    mainproductpage = MainProductPage(browser, link)
    itempage = ProductPage(browser, browser.current_url)
    
    mainproductpage.open() #Открываем страницу товара
    mainproductpage.should_be_add_to_basket_link() # Есть кнопка добавить в корзину
    
    mainproductpage.click_add_to_basket() #Наживаем добавить в корзину
    
    #time.sleep(5)
    itempage.should_not_be_success_message() # Проверяем, есть ли сообщение об успехе   
    

@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"])
def test_guest_cant_see_success_message(browser, link):    
   
    
    mainproductpage = MainProductPage(browser, link)
    itempage = ProductPage(browser, browser.current_url)
    
    mainproductpage.open()  #Открываем страницу товара
    itempage.should_not_be_success_message() # Проверяем, есть ли сообщение об успехе 
    #time.sleep(5)
      

@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"])
def test_message_disappeared_after_adding_product_to_basket(browser, link):    
   
    
    mainproductpage = MainProductPage(browser, link)
    itempage = ProductPage(browser, browser.current_url)
    
    mainproductpage.open()  #Открываем страницу товара
    mainproductpage.should_be_add_to_basket_link() # Есть кнопка добавить в корзину
    mainproductpage.click_add_to_basket() #Наживаем добавить в корзину
    itempage.should_success_message_diasppeared() # Проверяем, исчезло ли сообщение об успехе
      
    
    
    #time.sleep(5)
      





