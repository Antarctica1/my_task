from selenium import webdriver

keyword=input("이미지:")
url="https://www.google.co.kr/search?hl=ko&tbm=isch&q={}".format(keyword)
driver = webdriver.Chrome("C:\chromedriver.exe")
driver.implicitly_wait(15)
driver.maximize_window()

driver.get(url)