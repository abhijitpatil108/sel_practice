from selenium import webdriver
from selenium.webdriver import Chrome
from time import sleep
from requests import request
###############################################################################################################
'''           Web service Automation              '''
###############################################################################################################

'''finding broken links using web service automation'''
# driver = Chrome("./chromedriver")
# driver.maximize_window()
# driver.get("file:///D:/Abhi_TYSS/Python_Selenium/demo-html-20220303T044232Z-001/demo-html/links.html")
#
# sleep(5)
#
# links = driver.find_elements_by_tag_name("a")
# # print(links)
#
# urls = [link.get_attribute("href") for link in links]
# url_names =[item.text for item in links ]
# # for url, url_name in zip(urls, url_names):
# #     print((url,url_name))
# # print(url)
# # print(url_name)
# broken_links = []
# working_links = []
# for item, url_name in zip(urls,url_names):
#     # item_ele = driver.find_element_by_xpath(f"//a[@href='{item}']").text
#     r = request("GET", url = item)
#     if r.status_code == 200:
#         working_links.append(url_name)
#         # print(f"{item_ele} link is working fine")
#     else:
#         broken_links.append(url_name)
#         # print(f'link is broken for {item_ele} ')
# #
# print(f"broken_links are {broken_links}")
# print(f"working_links are {working_links}")

'''checking links under CATEGORIES are working fine or not'''

driver = Chrome("./chromedriver")
driver.maximize_window()
driver.get("http://demowebshop.tricentis.com/")
sleep(5)

links = driver.find_elements_by_xpath("//div[@class='block block-category-navigation']//a")
# print(len(links))
print(links)
link_names = [item.text for item in links]
urls = [item.get_attribute("href") for item in links]

for url,link_name in zip(urls,link_names):
    responce = request("GET", url = url)
    if responce.status_code == 200:
        print(f"{link_name} under CATEGORIES is working fine")
    else:
        print(f"{link_name} under CATEGORIES is broken")
