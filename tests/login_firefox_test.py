import time

from selenium import webdriver
# driver = webdriver.Chrome(executable_path="../drivers/geckodriver.exe")
driver = webdriver.Firefox(executable_path="../drivers/geckodriver.exe")
driver.implicitly_wait(5)
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.find_element_by_id("txtUsername").send_keys("Admin")
driver.find_element_by_id("txtPassword").send_keys("admin123")
driver.find_element_by_id("btnLogin").click()
time.sleep(5)
print("Test is completed")

