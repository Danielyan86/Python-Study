from selenium import webdriver
import logging
import time

DOCKER = False
current_time = time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime())
logging.basicConfig(filename="./log/selenium_deb_log_{0}".format(current_time), level=logging.DEBUG)

url = "http://www.google.com"
text_box_xpath = "//input[@id='lst-ib']"
search_button_xpath = "//input[@name='btnK']"

if DOCKER:
    d = webdriver.Chrome()
else:
    d = webdriver.Chrome(executable_path="./chromedriver")
d.get(url)
d.find_element_by_xpath(text_box_xpath).send_keys("test\n")
time.sleep(6)
# d.find_element_by_xpath(search_button_xpath).click()
# time.sleep(6)
#
# d.close()
