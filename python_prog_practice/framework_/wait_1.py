#
# from selenium.webdriver.support.expected_conditions import visibility_of_element_located
# from selenium.webdriver.remote.webdriver import WebElement
# from selenium.webdriver.support.wait import WebDriverWait
#
# from config_1 import Config
#
# class _visibility_of_element_located(visibility_of_element_located):
#     def __call_(self, driver):
#         print(driver)
#         result = super().__call__(self, driver)
#         if isinstance(result, WebElement):
#             return result.is_enabled()
#         return False
#
# def wait(func):
#     def wrapper(*args, **kwargs):  # args = (self, (By.ID,"FirstName"))
#         #args[0] = self
#         #args[1] = (By.ID,"FirstName")
#         instance = args[0]
#         locator = args[1]
#         wait = WebDriverWait(instance.driver, Config.TWP)
#         v = _visibility_of_element_located(locator)
#         wait.until(v)
#         return func(*args, **kwargs)
#     return wrapper


from selenium.webdriver.support.wait import WebDriverWait
from config_1 import Config
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.remote.webelement import WebElement

class _visibility_of_element_located(visibility_of_element_located):
    def __call__(self, driver):
        result = super().__call__(driver)
        if isinstance(result, WebElement):
            return result.is_enabled()
        return False

def wait(func):
    def wrapper(*args, **kwargs):
        # print(args[0])   # <selenium_wrapper_1.Selenium_Wrapper object at 0x02F95970>
        # print(args[1])   # ('class name', 'ico-register')
        instance = args[0]
        locator = args[1]
        wait = WebDriverWait(instance.driver, Config.WTP)
        v = _visibility_of_element_located(locator)
        wait.until(v)
        return func(*args, **kwargs)
    return wrapper
#
#
#
#
#





