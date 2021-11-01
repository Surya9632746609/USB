from selenium import webdriver
driver = webdriver.Chrome(executable_path="C://Users//surya//PycharmProjects//AutomationFrameWork_1//drivers//chromedriver.exe")
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://www.google.com/")
driver.find_element_by_name("q").send_keys("Hello Google")
driver.find_element_by_name("btnK").click()
print("Test is Completed")
