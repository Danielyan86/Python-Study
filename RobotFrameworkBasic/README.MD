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
 
## 练习
### 基础
- 运行Demo中的RF测试用例，理解测试用例和测试套件概念
- 创建测试数据，理解常量，变量等不同数据类型概念

### 进阶
- 运行并理解Demo中的测试用例
- 用python的方法创建一个API测试关键字
- 用python的类创建一个API测试关键字

### 综合
- 将以下测试用例步骤分别用UI和API自动化两种方式实现
- 登录Oscar Sandbox
- 在搜索框输入robot字符串并点击搜索
- 验证搜索结果
- 注销当前账号
