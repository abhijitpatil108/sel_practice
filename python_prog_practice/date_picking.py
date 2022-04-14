from selenium import webdriver
from selenium.webdriver import Chrome
from time import sleep, time
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.remote.webelement import WebElement



driver = Chrome("./chromedriver")
driver.maximize_window()
driver.get("https://www.goibibo.com/")
sleep(5)


# months = {'January':range(1,32), 'February':range(1,29), 'March':range(1,32), 'April':range(1,31), 'May':range(1,32), 'June':range(1,31), 'July':range(1,32), 'August':range(1,32), 'September':range(1,31), 'October':range(1,32), 'November':range(1,31), 'December':range(1,32)}
# lis = list(months.items())
# print(lis)

# b = months["February"]
# print(b)
# print(type(b))
# print(int("27") in b)




driver.find_element_by_xpath("//span[text()='Departure']").click()
sleep(2)
#
start_month = driver.find_element_by_xpath("//div[text()='March 2022']").text
# start_month = "March 2022"

_year ="2022"
_month = "November"
_day = "27"

months_lis1 = ['January 2022', 'February 2022', 'March 2022', 'April 2022', 'May 2022', 'June 2022', 'July 2022', 'August 2022', 'September 2022', 'October 2022', 'November 2022', 'December 2022']
months_lis2 = ['January 2023', 'February 2023', 'March 2023', 'April 2023', 'May 2023', 'June 2023', 'July 2023', 'August 2023', 'September 2023', 'October 2023', 'November 2023', 'December 2023']

months_lis = months_lis1+months_lis2
months_f = months_lis[(months_lis.index(start_month)):((months_lis.index(start_month))+12)]

if _month+_year not in months_f:
    print("You cannot book ticket for past months or more than a year advance")
else:
    for _ in range(12):
        try:
            _date = driver.find_element_by_xpath(f"//div[text()='{_month} {_year}']/../..//p[text()='{_day}']")
            print(_date.text)
            _date.click()
            sleep(2)
            driver.find_element_by_xpath("//span[text()='Done']").click()
            break
        except NoSuchElementException:
            driver.find_element_by_xpath("//span[@aria-label='Next Month']").click()
            sleep(2)
            continue
        except ElementClickInterceptedException:
            print("Date cannot a past date")
            break






