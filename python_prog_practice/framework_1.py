from selenium import webdriver
from selenium.webdriver import Chrome
from time import time, sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.remote.webelement import WebElement

# opts = webdriver.ChromeOptions
# opts.add_experimental_option()
#
#
# driver = Chrome("./chromedriver",options=opts)
# driver = Chrome("./chromedriver")

driver = Chrome("./chromedriver")
driver.maximize_window()
driver.get("http://demowebshop.tricentis.com/")
# sleep(2)
# driver.find_element().click()
# driver.find_element("id","small-searchterms").send_keys("hello")
# driver.find_element_by_link_text("Register").click()
#
class _visibility_of_element_located(visibility_of_element_located):
    def __call__(self, driver):
        result = super().__call__(driver)
        if isinstance(result, WebElement):
            return result.is_enabled()
        else:
            return False

def wait(func):
    def wrapper(*args, **kwargs):
        locator = args[0]
        wait = WebDriverWait(driver, 20)
        v = _visibility_of_element_located(locator)
        wait.until(v)
        return func(*args, **kwargs)
    return wrapper

@wait
def click_element(locator):
    driver.find_element(*locator).click()
    # driver.find_element("link_text","Register")

@wait
def enter_text(locator, *, value):
    driver.find_element(*locator).send_keys(value)

click_element(("link text","Register"))
click_element(('id','gender-male'))
enter_text(("id","FirstName"),value="abhi")
enter_text(("id","LastName"),value="patil")
enter_text(("id","Email"),value="abhi.patil@gmail.om")
enter_text(("id","Password"),value="12345678")
enter_text(("id","ConfirmPassword"),value="12345678")
click_element(("id","register-button"))


