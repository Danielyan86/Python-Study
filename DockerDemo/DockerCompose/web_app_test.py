import time

from selenium import webdriver

# DOCKER = False
# current_time = time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime())
# logging.basicConfig(filename="./log/selenium_deb_log_{0}".format(current_time), level=logging.DEBUG)
#

url = "web-app:80"
d = webdriver.Chrome()

d.get(url)
time.sleep(6)
d.close()
