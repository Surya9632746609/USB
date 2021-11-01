from selenium import webdriver
#browser exposes an executable file
#Through Selenium test we will invoke the executable file which will then #invoke actual browser
driver = webdriver.Chrome(executable_path="../drivers/chromedriver.exe")
# to maximize the browser window
driver.maximize_window()
#get method to launch the URL
driver.get("https://www.tutorialspoint.com/index.htm")
# to print the page title in console
print(driver.title)
# to print the current URL in console
print(driver.current_url)
#to refresh the browser
driver.refresh()
#to close the browser
driver.close()