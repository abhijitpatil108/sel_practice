from selenium import webdriver
from selenium.webdriver import Chrome
from time import time, sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.support.select import Select
from selenium.webdriver.remote.webdriver import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

driver = Chrome("./chromedriver")
driver.maximize_window()
driver.get("http://demowebshop.tricentis.com/")

class _visibility_of_element_located(visibility_of_element_located):
    def __call_(self):
        result = super().__call__(self)
        if isinstance(result, WebElement):
            return result.is_enabled()
        return False


def wait(func):
    def wrapper(*args, **kwargs):  # args = ((By.ID,"FirstName"),)
        # locator = args[0]
        # print(args)
        # print(*args)
        wait = WebDriverWait(driver, 20)
        v = _visibility_of_element_located(*args)
        wait.until(v)
        return func(*args, **kwargs)
    return wrapper


@wait  #click_element = wait(click_element)
def click_element(locator):
    # print(locator)
    driver.find_element(*locator).click()

@wait
def enter_text(locator, *, value):
    driver.find_element(*locator).send_keys(value)

click_element((By.CLASS_NAME,"ico-register"))
click_element((By.ID,"gender-male"))
enter_text((By.ID,"FirstName"),value="Abhi")
enter_text((By.ID,"LastName"),value="Patil")
enter_text((By.ID,"Email"),value="abhi.patil@gmail.om")
enter_text((By.ID,"Password"),value="123456789")
enter_text((By.ID,"ConfirmPassword"),value="123456789")

####################################################################################################
