# coding = utf-8
from selenium import webdriver
browser = webdriver.Chrome("C:\chromedriver\chromedriver.exe")
browser.get("https://www.soku.com")
# browser.find_element_by_id("headq").send_keys("天下无贼")
browser.find_element_by_xpath("//input[@id='headq']").send_keys("海阔天空")
browser.find_element_by_class_name("btn_search").click()

