from pom_demo_abhi.selenium_wrapper_pom_abhi import Selenium_Wrapper
from selenium.webdriver.common.by import By

class HomePage_(Selenium_Wrapper):
    _lgn_loc = (By.CLASS_NAME, 'ico-login')
    _reg_loc = (By.CLASS_NAME, 'ico-register')

    def __init__(self, driver):
        super().__init__(driver)

    def login_(self):
        self.driver.click_element(HomePage_._lgn_loc)

    def register(self):
        self.driver.click_element(HomePage_._reg_loc)