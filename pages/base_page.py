from selenium.webdriver import Remote as RemoteWebDriver

class BasePage():
    # Из комментов
    def __init__(self, browser: RemoteWebDriver, url, timeout=10):
        #def __init__(self, browser, url):
        self.browser = browser
        self.url = url
        self.browser.implicity_wait(timeout)
    
    def open(self):
        self.browser.get(self.url)
    