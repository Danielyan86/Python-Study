import logging
import time
import requests

from selenium import webdriver


def run_UI_test_in_local_env():
    # 引入日志模块，设置日志打印级别为debug，以便能打印更多的日志内容
    # 文件名后缀为执行脚本的起始时间
    current_time = time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime())
    logging.basicConfig(filename="./selenium_deb_log_{0}".format(current_time), level=logging.DEBUG)

    url = "http://www.bing.com"
    text_box_id = "sb_form_q"
    search_button_xpath = "//input[@name='btnK']"
    d = webdriver.Chrome()
    # 输入URL
    d.get(url)
    # 搜索框输入test
    d.find_element_by_id(text_box_id).send_keys("test\n")
    time.sleep(6)
    d.close()
    d.quit()


def run_UI_test_in_docker_env():
    # selenium grid方式远程运行
    current_time = time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime())
    logging.basicConfig(filename="./selenium_deb_log_{0}".format(current_time), level=logging.DEBUG)

    selenium_grid_url = "http://127.0.0.1:4444/wd/hub"
    capabilities = webdriver.DesiredCapabilities.CHROME.copy()
    d = webdriver.Remote(command_executor=selenium_grid_url, desired_capabilities=capabilities)

    url = "http://www.bing.com"
    text_box_id = "sb_form_q"
    # 输入URL
    d.get(url)
    # 搜索框输入test
    d.find_element_by_id(text_box_id).send_keys("test\n")
    time.sleep(10)
    d.close()
    d.quit()


if __name__ == '__main__':
    run_UI_test_in_local_env()
    # run_UI_test_in_docker_env()
