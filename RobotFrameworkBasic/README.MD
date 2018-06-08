ROBOT 
=====================

### Abstract
This project is used for robot framework study
=============
## install pip tool
 https://pip.pypa.io/en/stable/installing/
## install RF
pip install robotframework
## install selenium2library lib
pip install --upgrade robotframework-selenium2library

## 安装被测试环境
- 本机通过docker安装并启动被测试产品：docker run -p 8001:8000 -p 8086:8080 oscarcommerce/django-oscar-sandbox
- 安装Chrome webdriver（已经安装好的跳过）：
 http://npm.taobao.org/mirrors/chromedriver/
 https://sites.google.com/a/chromium.org/chromedriver/home
 复制驱动到本机可执行路径下面