# from selenium import webdriver
# from selenium.webdriver import Chrome
# from time import time, sleep
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.support.expected_conditions import visibility_of_element_located
# from selenium.webdriver.support.select import Select
# from selenium.webdriver.remote.webdriver import WebElement
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# # from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.common.keys import Keys
# from wait_1 import wait
#
# class Selenium_Wrapper_1:
#     def __init__(self, driver):
#         self.driver = driver
#         print(self.__dict__)
#         print(Selenium_Wrapper_1.__dict__)
#
#     @wait  # click_element = wait(click_element)
#     def click_element(self, locator):
#         print(locator)
#         self.driver.find_element(*locator).click()
#
#     @wait
#     def enter_text(self, locator, *, value):
#         self.driver.find_element(*locator).send_keys(value)

# from selenium import webdriver
# from selenium.webdriver.common.by import By
from wait_1 import wait

class Selenium_Wrapper:
    def __init__(self, driver):
        # print(self)      # <selenium_wrapper_1.Selenium_Wrapper object at 0x02F95970>
        self.driver = driver

    @wait
    def click_element(self, locator):
        self.driver.find_element(*locator).click()

    @wait
    def enter_text(self, locator, value):
        self.driver.find_element(*locator).send_keys(value)












