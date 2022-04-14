from selenium import webdriver
from selenium.webdriver import  Chrome
from time import sleep

driver = Chrome("./chromedriver")
driver.maximize_window()
driver.get("http://demowebshop.tricentis.com/")
sleep(3)

_email = "bill.gates@company.com"
_pass = "Password123"

driver.find_element_by_xpath("//a[text()='Log in']").click()
sleep(2)
driver.find_element_by_xpath("//input[@id='Email']").send_keys(_email)
driver.find_element_by_xpath("//input[@id='Password']").send_keys(_pass)
driver.find_element_by_xpath("//input[@value='Log in']").click()

for _ in range(10):
    try:
        target_ele = driver.find_element_by_xpath(f"//a[text()='{_email}']").text
        if target_ele == _email:
            print(f"logged in validation for {_email} is successfully")
            assert True
    except:
        sleep(1)
        print(f"logged in validation for {_email} is unsuccessful")
        continue
    # assert False


from 





# def is_user_logged_in():
#     if target_ele == _email:
#         return f"logged in validation for {_email} is successfully"
#     return f"logged in validation for {_email} is unsuccessful"

# def is_user_logged_in():
#     for _ in range(10):
#         try:
#             target_ele == _email
#             return f"logged in validation for {_email} is successfully"
#         except AssertionError:
#             sleep(1)
#             print(f"logged in validation for {_email} is unsuccessful")
#             continue
#     return False

# validating_user = is_user_logged_in()
# print(validating_user)
#






