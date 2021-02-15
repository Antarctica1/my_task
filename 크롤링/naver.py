#이미지
from selenium import webdriver

keyword=input("이미지:")
url="https://search.naver.com/search.naver?where=image&query={}".format(keyword)

driver=webdriver.Chrome("C:\chromedriver.exe")
driver.implicitly_wait(15)
driver.maximize_window()

driver.get(url)