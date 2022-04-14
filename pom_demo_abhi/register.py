from pom_demo_abhi.selenium_wrapper_pom_abhi import Selenium_Wrapper
from selenium.webdriver.common.by import By


class Register_(Selenium_Wrapper):
    reg_gender_locm = (By.ID, "gender-male")
    reg_gender_locf = (By.ID, "gender-female")
    reg_fname_loc = (By.ID, "FirstName")
    reg_lname_loc = (By.ID, "LastName")
    reg_email_loc = (By.ID, "Email")
    reg_pass_loc = (By.ID, "Password")
    reg_confirm_pass_loc = (By.ID, "ConfirmPassword")
    reg_reg_loc = (By.ID, "register-button")

    def __init__(self, driver):
        super().__init__(driver)

    def select_gender(self, gender):
        if gender == "male":
            self.driver.select_element(Register_.reg_gender_locm)
        else:
            self.driver.select_element(Register_.reg_gender_locf)

    def first_name(self, fname):
        self.driver.enter_text(Register_.reg_fname_loc,value=fname)

    def last_name(self, lname):
        self.driver.enter_text(Register_.reg_lname_loc,value=lname)

    def reg_email(self, email):
        self.driver.enter_text(Register_.reg_email_loc,value=email)

    def reg_pass(self, reg_pass):
        self.driver.enter_text(Register_.reg_pass_loc,value=reg_pass)

    def reg_confirm_pass(self, reg_confpass):
        self.driver.enter_text(Register_.reg_confirm_pass_loc,value=reg_confpass)

    def reg_register(self):
        self.driver.click_element(Register_.reg_reg_loc)

# s.click_element((By.CLASS_NAME,"ico-register"))
# s.click_element((By.ID,"gender-male"))
# s.enter_text((By.ID,"FirstName"),value="Abhi")
# s.enter_text((By.ID,"LastName"),value="Patil")
# s.enter_text((By.ID,"Email"),value="abhi.patil@gmail.om")
# s.enter_text((By.ID,"Password"),value="123456789")
# s.enter_text((By.ID,"ConfirmPassword"),value="123456789")
