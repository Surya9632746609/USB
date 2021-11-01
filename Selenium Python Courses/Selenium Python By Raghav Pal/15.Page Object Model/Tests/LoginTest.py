

from selenium import webdriver
import unittest
import time



driver = webdriver.Chrome(executable_path="C://Users//surya//PycharmProjects//AutomationFrameWork_1//drivers//chromedriver.exe")
driver.implicitly_wait(10)
driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
driver.maximize_window()
driver.find_element_by_id("txtUsername").send_keys("Admin")
driver.find_element_by_id("txtPassword").send_keys("admin123")
driver.find_element_by_id("btnLogin").click()
driver.find_element_by_id("welcome").click()
driver.find_element_by_link_text("Logout").click()
# driver.sleep()
driver.close()
driver.quit()
print("Test is completed")