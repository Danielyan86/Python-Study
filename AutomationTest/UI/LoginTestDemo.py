import time
import unittest

from selenium import webdriver


class MyTestCase(unittest.TestCase):
    def setUp(self):
        browser_type = input("input the browser type: ")  # 选择浏览器类型
        if browser_type == "ch":
            self.d = webdriver.Chrome()
        elif browser_type == "ff":
            self.d = webdriver.firefox

    def test_login_the_main_page(self):
        url = "http://127.0.0.1:8086/"
        self.d.get(url)
        time.sleep(4)
        self.d.find_element_by_id("login_link").click()
        time.sleep(6)
        self.d.find_element_by_name("login-username").send_keys("test@163.com")
        self.d.find_element_by_name("login-password").send_keys("Test123456")
        self.d.find_element_by_name("login_submit").click()
        self.d.find_element_by_xpath('//a[@href="/en-gb/accounts/"]')

    def tearDown(self):
        self.d.close()
        self.d.quit()


if __name__ == '__main__':
    unittest.main()
