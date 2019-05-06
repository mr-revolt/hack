# coding = utf-8
from selenium import webdriver
browser = webdriver.Chrome("C:\chromedriver\chromedriver.exe")
browser.get("https://baidu.com")
browser.find_element_by_name("wd").send_keys("revolt")
browser.find_element_by_id("su").click()
browser.quit()