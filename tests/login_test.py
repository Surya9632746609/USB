import time
from selenium import webdriver
import pytest

class TestLogin():
    @pytest.fixture(scope="class")
    def test_setup(self):
        global driver
        # driver = webdriver.Chrome(executable_path="../drivers/chromedriver.exe")
        driver = webdriver.Chrome(executable_path="C://Users//surya//PycharmProjects//AutomationFrameWork_1//drivers//chromedriver.exe")
        driver.implicitly_wait(5)
        driver.maximize_window()
        yield
        driver.close()
        driver.quit()
        print("Test Complete")


    def test_login(self, test_setup):
        driver.get("https://opensource-demo.orangehrmlive.com/")
        driver.find_element_by_id("txtUsername").send_keys("Admin")
        driver.find_element_by_id("txtPassword").send_keys("admin123")
        driver.find_element_by_id("btnLogin").click()

    def test_logout(self, test_setup):
        print(driver.title)
        driver.find_element_by_id("welcome").click()
        curUrl = driver.current_url
        print("Current Url is:"+driver.current_url)
        time.sleep(5)
        driver.find_element_by_link_text("Logout").click()
        print("Current Url is:"+driver.current_url)

    # url = driver.current_url
    # print(url)

    # url = driver.getCurrentUrl();
    # print(url)
