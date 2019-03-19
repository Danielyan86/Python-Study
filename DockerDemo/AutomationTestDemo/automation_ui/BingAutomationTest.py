import logging
import time

from selenium import webdriver

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
