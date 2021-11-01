from selenium import webdriver
import unittest
import HtmlTestRunner


class GoogleSearch(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="C:\\Users\\surya\\PycharmProjects\\AutomationFrameWork_1\\drivers\\chromedriver.exe")
        cls.driver.maximize_window()
        cls.driver.set_page_load_timeout(10)
        cls.driver.implicitly_wait(10)

    def test_Search3(self):
        self.driver.get("https://www.google.com/")
        self.driver.find_element_by_name("q").send_keys("Hello Google")
        self.driver.find_element_by_name("btnK").click()
        x = self.driver.title
        print(x)
        self.assertEqual(x, "Hello Google - Google Search")


    def test_Search4(self):
        self.driver.get("https://www.google.com/")
        self.driver.find_element_by_name("q").send_keys("Hello")
        self.driver.find_element_by_name("btnK").click()
        y = self.driver.title
        print(y)
        self.assertEqual(y, "Hello - Google Search")

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test is completed")

if __name__ == '__main__':
    # unittest.main(verbosity=2)
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\\Users\\surya\\PycharmProjects\\AutomationFrameWork_1\\Selenium Python Courses\\Selenium Python By Raghav Pal\\HTML Test Reports'))
