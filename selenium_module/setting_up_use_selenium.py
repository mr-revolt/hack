# coding = utf-8
from selenium import webdriver
driver = webdriver.Chrome("C:\chromedriver\chromedriver")
driver.get('https://google.com')
print(driver.title)
driver.quit()