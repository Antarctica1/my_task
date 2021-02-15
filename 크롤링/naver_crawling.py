#네이버 이미지 검색
from selenium import webdriver
import time

keyword = input("이미지:")
url="https://search.naver.com/search.naver?where=image&query={}".format(keyword)
driver = webdriver.Chrome("C:\chromedriver.exe")

driver.implicitly_wait(10)
driver.maximize_window()

driver.get(url)