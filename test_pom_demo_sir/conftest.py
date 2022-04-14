from selenium.webdriver import Chrome
from time import sleep
# from config_pom import Config
from pytest import fixture

# Fixture
@fixture
def _driver():
    # Launches a new chrome browser
    driver = Chrome("./chromedriver")
    driver.maximize_window()
    driver.get("http://demowebshop.tricentis.com/")
    sleep(3)
    yield driver        # passes the driver instance to all the test methods
    driver.quit()

# @fixture
# def hello():
#     return "hello world"