from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re
driver = webdriver.Chrome(".\chromedriver")
driver.get("https://www.ajio.com/")
driver.find_element_by_xpath("//input[@placeholder='Search AJIO']").send_keys("Shoes")
driver.find_element_by_xpath("//span[@class='ic-search']").click()
shoes_ = driver.find_elements_by_xpath("//div[@class='contentHolder']")
shoe_names = shoes_[:6]
for shoe in shoe_names:
    print(shoe.text)
original_price = [int("".join(re.findall(r"\d",item.text))) for item in driver.find_elements_by_xpath("//span[@class='orginal-price']")[:6]]
index = original_price.index(max(original_price))
shoe_names[index].click()

print("the highest original price shoe is")
print("________")
print(shoe_names[index].text)

