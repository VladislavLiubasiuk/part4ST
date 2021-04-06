from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import MainPageLocators
from pages.login_page import LoginPage

class MainPage(BasePage): 
    def go_to_login_page(self):
        link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        link.click()
        alert = self.browser.switch_to.alert #failsafe если вдруг появиться алерт? (тест упадет так как метод не обрабативает их)
        alert.accept()
        #return LoginPage(browser=self.browser, url=self.browser.current_url)
        
    def should_be_login_link(self):
        self.browser.find_element(*MainPageLocators.LOGIN_LINK), "Login link is not presented"