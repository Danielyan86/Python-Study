import unittest
import time
from selenium import webdriver


class TestBingHomepage(unittest.TestCase):
    REMOTE = True  # if the REMOTE value is true, the test runs in docker UI environment

    # REMOTE = False

    def setUp(self):
        if self.REMOTE:
            selenium_grid_url = "http://localhost:24444/wd/hub"  # 注意此时在测试容器里面，内部调用端口为24444
            capabilities = webdriver.DesiredCapabilities.CHROME.copy()
            self.d = webdriver.Remote(command_executor=selenium_grid_url, desired_capabilities=capabilities)
        else:
            self.d = webdriver.Chrome()
            self.d.implicitly_wait(10)

    def test_bing(self):
        print("start test")
        bing_url = "https://bing.com"

        self.d.get(bing_url)
        self.d.find_element_by_id("sb_form_q")  # 验证输入框
        self.d.implicitly_wait(10)

    # 关闭浏览器
    def tearDown(self):
        time.sleep(10)
        self.d.close()
        self.d.quit()


if __name__ == '__main__':
    unittest.main()
