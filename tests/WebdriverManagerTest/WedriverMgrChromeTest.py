import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(5)
driver.get("https://www.google.com/")
time.sleep(5)
driver.title
print(driver.title)
print("Test is completed")
driver.close()
driver.quit()