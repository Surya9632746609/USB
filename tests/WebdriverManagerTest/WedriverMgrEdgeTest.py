import time

from selenium import webdriver

from webdriver_manager.microsoft import EdgeChromiumDriverManager

driver = webdriver.Edge(EdgeChromiumDriverManager().install())

driver.implicitly_wait(5)
driver.get("https://www.google.com/")
time.sleep(5)
driver.title
print(driver.title)
print("Test is completed")
driver.close()
driver.quit()