# from selenium import webdriver
from selenium.webdriver import Chrome
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
import re

driver = Chrome("./chromedriver")
driver.maximize_window()
driver.get("https://www.ajio.com/")
# sleep(5)
driver.implicitly_wait(10)

action_ = ActionChains(driver)

men = driver.find_element_by_xpath("//a[@title='MEN']")
action_.move_to_element(men).perform()
footware = "(//span[text()='FOOTWEAR & ACCESSORIES'])[1]"
driver.find_element_by_xpath(footware).click()
sleep(5)

shoes_elements = driver.find_elements_by_xpath("//div[@class='contentHolder']")
shoes_ = [shoe.text for shoe in shoes_elements]
print(shoes_)

'''so = [r'RED TAPE\nLace-Up Walking Shoes with Pull-Up Tabs\n₹1,568 ₹4,899 (68% off)\nSale Price ₹1470', 'RED TAPE\nLow-Top Lace-Up Walking Shoes\n₹1,225 ₹4,899 (75% off)\nSale Price ₹1224', 'RED TAPE\nHeathered Lace-Up Sports Shoes\n₹1,888 ₹5,899 (68% off)\nSale Price ₹1770', 'RED TAPE\nLow-Top Lace-Up Walking Shoes\n₹1,225 ₹4,899 (75% off)\nSale Price ₹1224', 'RED TAPE\nLow-Top Lace-Up Walking Shoes\n₹1,225 ₹4,899 (75% off)\nSale Price ₹1224', 'RED TAPE\nLace-Up Sports Shoes\n₹2,100 ₹6,999 (70% off)\nSale Price ₹2099', 'RED TAPE\nLace-Up Sports Shoes\n₹2,190 ₹7,299 (70% off)\nSale Price ₹2189', 'RED TAPE\nTextured Lace-Up Shoes\n₹2,240 ₹6,999 (68% off)\nSale Price ₹2100', 'U.S. Polo Assn.\nLebron 2.0 Lace-Up Sneakers\n₹2,399 ₹3,999 (40% off)\nSale Price ₹2039', 'RED TAPE\nGeometric Pattern Pool Slides\n₹704 ₹2,199 (68% off)\nSale Price ₹660', 'RED TAPE\nSlip-On Sliders with Logo Branding\n₹660 ₹2,199 (70% off)\nSale Price ₹659', 'RED TAPE\nTextured Lace-Up Sports Shoes\n₹2,190 ₹7,299 (70% off)\nSale Price ₹2189', 'RED TAPE\nHeathered Lace-Up Sports Shoes\n₹1,225 ₹4,899 (75% off)\nSale Price ₹1224', 'RED TAPE\nLace-Up Walking Shoes\n₹1,568 ₹4,899 (68% off)\nSale Price ₹1470', 'RED TAPE\nColourblock Slides with Brand Print\n₹704 ₹2,199 (68% off)\nSale Price ₹660', 'Puma\nDwane Idp Lace-Up Running Shoes\n₹1,600 ₹3,999 (60% off)\nSale Price ₹1200', 'WILDHORN\nWH2052 Genuine Leather Bi-Fold Wallet\n₹300 ₹1,499 (80% off)\nSale Price ₹300', 'Campus\nFlat Heel Sports Shoes\n₹1,529 ₹1,799 (15% off)\nSale Price ₹1528', 'RED TAPE\nLace-Up Sneakers with Perforations\n₹1,410 ₹4,699 (70% off)\nSale Price ₹1175', 'RED TAPE\nTextured Lace-Up Sports Shoes\n₹1,825 ₹7,299 (75% off)\nSale Price ₹1824', 'RED TAPE\nLow-Top Lace-Up Sneakers\n₹1,410 ₹4,699 (70% off)\nSale Price ₹1409', 'LEVIS\nTextured Lace-Up Sneakers\n₹1,500 ₹2,999 (50% off)\nSale Price ₹1275', 'RED TAPE\nTape Pool Slides with Brand Print\n₹600 ₹1,999 (70% off)\nSale Price ₹599', 'RED TAPE\nLow-Top Lace-Up Walking Shoes\n₹1,225 ₹4,899 (75% off)\nSale Price ₹1224', 'WILDHORN\nLeather Bi-Fold Wallet\n₹300 ₹1,499 (80% off)\nSale Price ₹300', 'Campus\nNorth Plus Lace-Up Running Sports Shoes\n₹1,444 ₹1,699 (15% off)\nSale Price ₹1443', 'Puma\nSkipper IDP Lace-Up Running Shoes\n₹1,935 ₹4,299 (55% off)\nSale Price ₹1462', 'CROCS\nBayaband Slingback Clogs\n₹2,447 ₹3,495 (30% off)\nSale Price ₹1713', 'RED TAPE\nLogo Embossed Pool Slides\n₹600 ₹1,999 (70% off)\nSale Price ₹599', 'U.S. Polo Assn.\nClarkin Low-Top Lace-Up Shoes\n₹1,649 ₹2,999 (45% off)\nSale Price ₹1402', 'RED TAPE\nPanelled Lace-Up Walking Shoes\n₹1,632 ₹5,099 (68% off)\nSale Price ₹1530', 'RED TAPE\nLace-Up Walking Shoes with Pull-Up Tabs\n₹1,225 ₹4,899 (75% off)\nSale Price ₹1224', 'RED TAPE\nPanelled Low-Top Lace-Up Walking Shoes\n₹1,856 ₹5,799 (68% off)\nSale Price ₹1740', 'Campus\nCity-Ride Textured Low-Top Lace-Up Sports Shoes\n₹1,359 ₹1,699 (20% off)\nSale Price ₹951', 'Campus\nRim Lace-Up Running Shoes\n₹1,599 ₹1,999 (20% off)\nSale Price ₹1119', 'CROCS\nBayaband Slingback Clogs\n₹2,447 ₹3,495 (30% off)\nSale Price ₹1713', 'U.S. Polo Assn.\nLebron 2.0 Lace-Up Sneakers\n₹2,399 ₹3,999 (40% off)\nSale Price ₹2039', 'RED TAPE\nTextured Lace-Up Sports Shoes\n₹2,190 ₹7,299 (70% off)\nSale Price ₹2189', 'ARBUNORE\nLace-Up Casual Shoes\n₹1,320 ₹3,299 (60% off)\nSale Price ₹990', 'Skechers\nUltra Flex 2.0 Casual Shoes\n₹3,499 ₹4,999 (30% off)\nSale Price ₹3498', 'Puma\nDwane IDP Lace-Up Sports Shoes\n₹1,600 ₹3,999 (60% off)\nSale Price ₹1200', 'WOODLAND\nCasual Sandals with Detachable Strap\n₹1,887 ₹2,695 (30% off)\nSale Price ₹1886', 'RED TAPE\nTextured Lace-Up Sports Shoes\n₹1,568 ₹4,899 (68% off)\nSale Price ₹1470', 'Puma\nPropel EL IDP High-Risk Lace-Up Casual Shoes\n₹1,800 ₹3,999 (55% off)\nSale Price ₹1360', 'Campus\nOslo Lace-Up Running Shoes\n₹1,319 ₹1,649 (20% off)\nSale Price ₹923']'''
prices = []
for item in shoes_:
    price = re.findall(r"[\d\,]+",item)
    prices.append(price)

# print(prices)

for item in prices:
    for price in item:
        res = re.findall(r"\d+", price)
        item[item.index(price)] = "".join(res)

print(prices)



# prices_s = list(sorted(prices, key=lambda item: item[-1]))
# print(prices_s)

