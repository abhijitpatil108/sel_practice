from pom_demo_abhi.selenium_wrapper_pom_abhi import Selenium_Wrapper
from selenium.webdriver.common.by import By

class Login_(Selenium_Wrapper):
    _log_eml = (By.ID, "Email")
    _log_pass = (By.ID, "Password")
    _log_log = (By.CLASS_NAME, "button-1 login-button")

    def __init__(self, driver):
        super().__init__(driver)

    def log_email(self, email):
        self.driver.enter_text(Login_._log_eml, value=email)

    def log_password(self, password):
        self.driver.enter_text(Login_._log_pass, value=password)

    def log_login(self):
        self.click_element(Login_._log_log)