from selenium.webdriver import Remote as RemoteWebDriver

from selenium.common.exceptions import NoSuchElementException


class BasePage():
    # Из комментов
    def __init__(self, browser: RemoteWebDriver, url, timeout=10):
        #def __init__(self, browser, url):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)
    
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True
    
    def open(self):
        self.browser.get(self.url)
    