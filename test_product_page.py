import time, pytest
#from pages.main_page import MainPage # иногда в начале нужна точка
#from pages.main_page import MainPage
from pages.product_page import ProductPage # иногда в начале нужна точка
from pages.basket_page import BasketPage
from pages.base_page import BasePage
from pages.login_page import LoginPage

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


@pytest.mark.skip   # из предыдущего задания                           
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"])
#7 - с ошибкой
    
def test_guest_can_add_product_to_basket(browser, link):
#def test_guest_can_add_product_to_basket(browser):
    
    #browser.delete_all_cookies()  # очистка кукисов
       
    #link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    #link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    
    
    itempage = ProductPage(browser, link)
    
    itempage.open()  #Открываем страницу товара
    itempage.should_not_be_success_message() # проверяем что нет сообщения о добавлении в корзину(мы только вошли на страницу) 4 сек. ожидание по-умолчанию
    
    
    itempage.should_be_add_to_basket_link() # Есть кнопка добавить в корзину
    
    itempage.click_add_to_basket() #Наживаем добавить в корзину
    itempage.solve_quiz_and_get_code()  # Нужен алерт для этого метода - решаем, вставляем значение 
    #time.sleep(5)
        
    
    itempage.should_be_proper_item() # проверяем что в корзину добавлен правильный товар
    
    #itempage.should_not_be_success_message() #Упадет с ошибкой т.к. товар добавлен и SUCCESS_MESSAGE есть на странице
  
@pytest.mark.skip   # из предыдущего задания  
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209"])
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, link):    
   
    
    itempage = ProductPage(browser, link)
    
    itempage.open() #Открываем страницу товара
    itempage.should_be_add_to_basket_link() # Есть кнопка добавить в корзину
    
    itempage.click_add_to_basket() #Наживаем добавить в корзину
    
    #time.sleep(5)
    itempage.should_not_be_success_message() # Проверяем, есть ли сообщение об успехе   
    
@pytest.mark.skip   # из предыдущего задания  
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"])
def test_guest_cant_see_success_message(browser, link):    
   
    
    mainproductpage = MainProductPage(browser, link)
    itempage = ProductPage(browser, browser.current_url)
    
    mainproductpage.open()  #Открываем страницу товара
    itempage.should_not_be_success_message() # Проверяем, есть ли сообщение об успехе 
    #time.sleep(5)
      
@pytest.mark.skip   # из предыдущего задания  
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"])
def test_message_disappeared_after_adding_product_to_basket(browser, link):    
   
    
    mainproductpage = MainProductPage(browser, link)
    itempage = ProductPage(browser, browser.current_url)
    
    mainproductpage.open()  #Открываем страницу товара
    mainproductpage.should_be_add_to_basket_link() # Есть кнопка добавить в корзину
    mainproductpage.click_add_to_basket() #Наживаем добавить в корзину
    itempage.should_success_message_diasppeared() # Проверяем, исчезло ли сообщение об успехе
    #time.sleep(5)
      
@pytest.mark.skip   # из предыдущего задания  
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"])
def test_guest_should_see_login_link_on_product_page(browser, link):
    page = MainProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.skip   # из предыдущего задания  
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"])
def test_guest_can_go_to_login_page_from_product_page(browser, link):
    page = MainProductPage(browser, link)
    page.open()
    page.should_be_login_link()
    page.go_to_login_page()

@pytest.mark.skip   # из предыдущего задания  
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"])
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser, link):
    
    basketpage=BasketPage(browser, link)
    basketpage.open()
    basketpage.should_be_basket_link()
    basketpage.go_to_basket_page()
    basketpage.should_be_no_items_in_basket()
    #time.sleep(5)


@pytest.mark.skip   # проверка регистрации
#@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"])
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"])

def test_guest_can_see_login_page(browser, link):
    
    loginpage=LoginPage(browser, link)
    loginpage.open()
    loginpage.should_be_login_link()
    loginpage.go_to_login_page()
    loginpage.should_be_login_page()
    
    email = str(time.time()) + "@fakemail.org"
    password= "1qaz2wsx3edc_"
    
    loginpage.should_be_register_button()
    loginpage.register_new_user(email,password)
    loginpage.click_register_button()
    loginpage.should_be_authorized_user()
        
    #time.sleep(5)



link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"

#class TestLoginFromMainPage(MainPage):
class TestUserAddToBasketFromProductPage(object):

    
#---------------------------------------------------------
    @pytest.fixture(scope="function", autouse=True) # scope="class" "function"
    def setup(self, browser):
        
        loginpage = LoginPage(browser, link)
        loginpage.open()
        loginpage.should_be_login_link()
        loginpage.go_to_login_page()
        loginpage.should_be_login_page()
    
        email = str(time.time()) + "@fakemail.org"
        password= "1qaz2wsx3edc_"
    
        loginpage.should_be_register_button()
        loginpage.register_new_user(email,password)
        loginpage.click_register_button()
        loginpage.should_be_authorized_user()
        #time.sleep(30)
#        
#        self.product = ProductFactory(title = "Best book created by robot")
#        # создаем по апи
#        self.link = self.product.link
#        yield
#        # после этого ключевого слова начинается teardown
#        # выполнится после каждого теста в классе
#        # выполнится после каждого теста в классе
#        # удаляем те данные, которые мы создали 
#        self.product.delete()
#----------------------------------------------------------
        
    def test_user_cant_see_success_message(self, browser):    
   
        itempage = ProductPage(browser, link)
    
        itempage.open() #Открываем страницу товара
        itempage.should_not_be_success_message() # проверяем что нет сообщения о добавлении в корзину в самом начале
      
        

    def test_user_can_add_product_to_basket(self, browser):

        #browser.delete_all_cookies()  # очистка кукисов
        
        itempage = ProductPage(browser, link)
        itempage.open()  #Открываем страницу товара
        itempage.should_not_be_success_message() # проверяем что нет сообщения о добавлении в корзину в самом начале
        itempage.should_be_add_to_basket_link() # Есть кнопка добавить в корзину
    
        itempage.click_add_to_basket() #Нажимаем добавить в корзину
        itempage.solve_quiz_and_get_code()  # решаем, вставляем значение 
        #time.sleep(5)
        itempage.should_be_proper_item() # проверяем что в корзину добавлен правильный товар



#---------------------

'''

#Мы уже немного говорили про независимость от контента в предыдущих шагах — идеальным решением было бы везде, где мы #работаем со страницей продукта, создавать новый товар в нашем интернет-магазине перед тестом и удалять по завершении #теста.# К сожалению, наш интернет-магазин пока не имеет возможности создавать объекты по API, но в идеальном мире мы бы #написали вот такой тест-класс


@pytest.mark.login
class TestLoginFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        self.product = ProductFactory(title = "Best book created by robot")
        # создаем по апи
        self.link = self.product.link
        yield
        # после этого ключевого слова начинается teardown
        # выполнится после каждого теста в классе
        # удаляем те данные, которые мы создали 
        self.product.delete()
        

    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        page = ProductPage(browser, self.link)
        # дальше обычная реализация теста

    def test_guest_should_see_login_link(self, browser):
        page = ProductPage(browser, self.link)
        # дальше обычная реализация тест


'''    