"""
5. FIRST SELENIUM TEST

First Selenium Python test
Today we will:
1.Create a new project in PyCharm
2.Add Selenium scripts
3.Add Browser driver
4.Run and Validate
"""
from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="C://Users//surya//PycharmProjects//AutomationFrameWork_1//drivers//chromedriver.exe")
#driver = webdriver.Chrome(executable_path="C://Users//surya//PycharmProjects//AutomationFrameWork_1//drivers//chromedriver.exe")
driver.maximize_window()
driver.set_page_load_timeout(10)
driver.get("https://www.google.com/")
driver.find_element_by_name("q").send_keys("Hello Google")
time.sleep(5)
driver.find_element_by_name("btnK").click()
driver.close()
driver.quit()
print("Test is Complete")

