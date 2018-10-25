import unittest
import time
from selenium import webdriver


class TestBingHomepage(unittest.TestCase):
    REMOTE = True  # if the REMOTE value is true, the test runs in docker UI environment

    def test_bing(self):
        print("start test")
        bing_url = "https://bing.com"

        if self.REMOTE:
            selenium_grid_url = "http://127.0.0.1:4444/wd/hub"
            capabilities = webdriver.DesiredCapabilities.CHROME.copy()
            self.d = webdriver.Remote(command_executor=selenium_grid_url, desired_capabilities=capabilities)
        else:
            self.d = webdriver.Chrome()
            self.d.implicitly_wait(10)
        self.d.get(bing_url)
        self.d.implicitly_wait(10)

    def tearDown(self):
        time.sleep(10)
        self.d.close()
        self.d.quit()


if __name__ == '__main__':
    unittest.main()
