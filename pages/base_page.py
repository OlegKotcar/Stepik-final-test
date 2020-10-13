from selenium.webdriver import Remote as RemoteWebDriver

class BasePage():
    # Из комментов
    def __init__(self, browser: RemoteWebDriver, url):
        #def __init__(self, browser, url):
        self.browser = browser
        self.url = url
    
    def open(self):
        self.browser.get(self.url)
    