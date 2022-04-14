from selenium import webdriver
from selenium.webdriver import Chrome
from time import time,sleep
from selenium.webdriver.common.action_chains import ActionChains

driver = Chrome("./chromedriver")
driver.maximize_window()
driver.get("https://www.monsterindia.com/")
sleep(5)

action_ = ActionChains(driver)

webelement1= driver.find_element_by_xpath("//a[text()='Job search']")
action_.move_to_element(webelement1).perform()
webelement2 = driver.find_element_by_xpath("//a[text()='Jobs by Skills']")
action_.move_to_element(webelement2).perform()
webelement3 = driver.find_element_by_xpath("//a[contains(text(),'Devops Jobs')]")
action_.move_to_element(webelement3).perform()
webelement3.click()
sleep(2)
