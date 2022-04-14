from logging import exception
import exception


import  selenium
from selenium import webdriver
from selenium.webdriver import Chrome
from time import sleep, time
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.common.exceptions import NoSuchElementException

driver = Chrome("./chromedriver")
driver.maximize_window()
# driver.get("https://www.monsterindia.com/")
driver.get("https://twitter.com/")
sleep(5)
# item = driver.find_element_by_xpath("(//span[text()='Sign up with Google'])[1]")
driver.find_element_by_xpath("(//div[@id='container']/../../..//span[text()='Sign up with Google'])[1]").click()

sleep(2)



# driver.find_element_by_xpath("//span[text()='Upload Resume']").click()
# sleep(2)
# driver.find_element_by_xpath("(//input[@id='file-upload'])[2]").send_keys(r"C:\Users\Abhijit\Desktop\Method_Table.docx")
# # driver.find_element_by_xpath("(//button[text()='Or select file to upload'])[1]").send_keys(r"C:\Users\Abhijit\Desktop\Method_Table.docx")
# sleep(5)
# driver.find_element_by_xpath("(//input[@value='Submit'])[1]").click()
# # driver.find_element_by_xpath("(//input[@value='Submit'])[1]").click()
# sleep(2)