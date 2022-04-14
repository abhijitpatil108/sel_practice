from selenium_wrapper_pom import Selenium_Wrapper

class RegistrationPage(Selenium_Wrapper):
    _rdo_male = ("id", "gender-male")
    _rdo_female = ("id", "gender-female")
    _txt_first_name = ("name", "FirstName")
    _txt_last_name = ("name", "LastName")
    _txt_email = ("id", "Email")
    _txt_password = ("id", "Password")
    _txt_confirm_password = ("id", "ConfirmPassword")
    _btn_register = ("id", "register-button")

    def __init__(self, driver):
        super().__init__(driver)
    
    def registration_select_male(self):
        self.click_element(RegistrationPage._rdo_male)
    
    def registration_select_female(self):
        self.click_element(RegistrationPage._rdo_female)

    def registration_enter_first_name(self, fname):
        self.enter_text(RegistrationPage._txt_first_name, value=fname)
    
    def registration_enter_last_name(self, lname):
        self.enter_text(RegistrationPage._txt_last_name, value=lname)
    
    def registration_enter_email(self, email):
        self.enter_text(RegistrationPage._txt_email, value=email)
    
    def registration_enter_password(self, password):
        self.enter_text(RegistrationPage._txt_password, value=password)
    
    def registration_enter_confirm_password(self, password):
        self.enter_text(RegistrationPage._txt_confirm_password, value=password)
    
    def registation_click_register(self):
        self.click_element(RegistrationPage._btn_register)
    