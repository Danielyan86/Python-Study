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
        user_name = "test@163.com"
        pass_word = "Test123456"
        account_xpath = '//a[@href="/en-gb/accounts/"]'
        self.d.get(url)
        time.sleep(4)
        self.d.find_element_by_id("login_link").click()
        time.sleep(6)
        self.d.find_element_by_name("login-username").send_keys(user_name)
        self.d.find_element_by_name("login-password").send_keys(pass_word)
        self.d.find_element_by_name("login_submit").click()
        self.d.find_element_by_xpath(account_xpath)

    def tearDown(self):
        self.d.close()
        self.d.quit()


if __name__ == '__main__':
    unittest.main()
