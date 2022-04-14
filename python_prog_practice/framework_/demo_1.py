# from selenium import webdriver
# from selenium.webdriver import Chrome
# from time import time, sleep
# from selenium.webdriver.common.by import By
# from config_1 import Config
# from selenium_wrapper_1 import Selenium_Wrapper_1
#
# driver = Chrome("./chromedriver")
# driver.maximize_window()
# driver.get(Config.URL)
# # driver.get("http://demowebshop.tricentis.com/")
#
# s = Selenium_Wrapper_1(driver)
#
# s.click_element((By.CLASS_NAME,"ico-register"))
# s.click_element((By.ID,"gender-male"))
# s.enter_text((By.ID,"FirstName"),value="Abhi")
# s.enter_text((By.ID,"LastName"),value="Patil")
# s.enter_text((By.ID,"Email"),value="abhi.patil@gmail.om")
# s.enter_text((By.ID,"Password"),value="123456789")
# s.enter_text((By.ID,"ConfirmPassword"),value="123456789")


from selenium.webdriver import Chrome
from time import time, sleep
from config_1 import Config
from selenium_wrapper_1 import Selenium_Wrapper
from selenium.webdriver.common.by import By

driver = Chrome("./chromedriver")
driver.maximize_window()
driver.get(Config.URL)


s = Selenium_Wrapper(driver)
s.click_element((By.CLASS_NAME,"ico-register"))
s.click_element((By.ID,"gender-male"))
s.enter_text((By.ID,"FirstName"),value="Abhi")
s.enter_text((By.ID,"LastName"),value="Patil")
s.enter_text((By.ID,"Email"),value="abhi.patil@gmail.om")
s.enter_text((By.ID,"Password"),value="123456789")
s.enter_text((By.ID,"ConfirmPassword"),value="123456789")
# print(s)  # <selenium_wrapper_1.Selenium_Wrapper object at 0x02F95970>