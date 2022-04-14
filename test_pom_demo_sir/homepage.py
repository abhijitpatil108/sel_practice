from test_pom_demo_sir.selenium_wrapper_pom import Selenium_Wrapper
from selenium import  webdriver
from time import sleep

class HomePage(Selenium_Wrapper):
    _lnk_register = ("link text", "Register")
    _lnk_login = ("link text", "Log in")

    def __init__(self, driver):
        super().__init__(driver)
    
    def home_click_register(self):
        self.click_element(HomePage._lnk_register)
    
    def home_click_login(self):
        self.click_element(HomePage._lnk_login)

    # def is_user_logged_in(self, email):
    #     target_ele = self.driver.find_element_by_xpath(f"//a[text()={email}]").text
    #     #//a[text()='bill.gates@company.com']
    #     # _xpath = self.driver.find_element_by_xpath(f"//a[text()={email}]")
    #     for _ in range(10):
    #         try:
    #             target_ele == email
    #             return f"logged in validation for {email} is successfully"
    #         except AttributeError:
    #             sleep(1)
    #             print(f"logged in validation for {email} is unsuccessful")
    #             continue
    #     return False