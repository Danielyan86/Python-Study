# ROBOT framework

### Abstract

# This project is used for robot framework study

## install pip tool

https://pip.pypa.io/en/stable/installing/

## install RF

pip install robotframework

## install seleniumlibrary lib

- pip install robotframework-selenium2library
- pip install --upgrade robotframework-seleniumlibrary
- 无法用 pip 安装 robot 的，直接下载源码安装包到本地安装 https://github.com/robotframework/robotframework/releases

## 安装被测试环境

- 本机通过 docker 安装并启动被测试产品：docker run -p 8001:8000 -p 8080:8080 oscarcommerce/django-oscar-sandbox
- oscarcommerce/django-oscar-sandbox 产品代码库 https://github.com/django-oscar/django-oscar
- 安装 Chrome webdriver（已经安装好的跳过）：
  http://npm.taobao.org/mirrors/chromedriver/
  https://sites.google.com/a/chromium.org/chromedriver/home
  下载 chrome 驱动程序并复制到系统默认路径下，比如 Linux 系统复制到/usr/local/bin

## RF 相关文档

- 官方网站 http://robotframework.org/
- 用户手册 http://robotframework.org/robotframework/#user-guide

## 练习

### 基础

- 运行 Demo 中的 RF 测试用例，理解测试用例和测试套件概念
  - UI_demo 需要提前注册一个账号
- 创建测试数据，理解常量，变量等不同数据类型概念
- 导入第三方库并运行其中的一个关键字
  http://robotframework.org/Selenium2Library/Selenium2Library.html#Click%20Link
  http://robotframework.org/robotframework/latest/libraries/Collections.html
- 创建一个用户自定义关键字并运行
- 执行一个测试用例并修改输出的 log 名字
- 查看并理解测试报告

### 进阶

- 运行并理解 Demo 中的测试用例
- 用 python 的方法创建一个 API 测试关键字
- 用 python 的类创建一个 API 测试关键字

### 综合

- 将以下测试用例步骤分别用 UI 和 API 自动化两种方式实现
- 登录 Oscar Sandbox
- 在搜索框输入 robot 字符串并点击搜索
- 验证搜索结果
- 注销当前账号
