from selenium import webdriver
from selenium.webdriver import Chrome
from pom_demo_abhi.config_1 import Config
from pytest import fixture
from time import sleep

@fixture()
def _driver():
    driver = Chrome("./chromedriver")
    driver.maximize_window()
    driver.get(Config.URL)
    sleep(3)
    yield driver
    driver.quit()

