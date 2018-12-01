import logging
import time

from selenium import webdriver

# DOCKER = False
current_time = time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime())
logging.basicConfig(filename="./selenium_deb_log_{0}".format(current_time), level=logging.DEBUG)

url = "http://www.bing.com"
# text_box_xpath = "//input[@id='lst-ib']"
text_box_id="sb_form_q"
search_button_xpath = "//input[@name='btnK']"
d = webdriver.Chrome()
d.get(url)
d.find_element_by_id(text_box_id).send_keys("test\n")
time.sleep(6)
d.close()
d.quit()