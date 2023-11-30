# 环境安装

## 命令行工具

- Curl(linux 自带) https://curl.haxx.se/download.html
- httpie - https://github.com/jakubroztocil/httpie

## 图形化测试工具

- postman - https://www.postman.com/downloads/
- nodejs - https://nodejs.org/en/download/
- newman - https://www.npmjs.com/package/newman
  - npm install - g newman

## 自动化测试框架

httprunner - https://github.com/httprunner/httprunner

## 课程实验环境安装

- python https://www.python.org/downloads/
- python requests 安装 pip install requests
- Django https://www.djangoproject.com/download/
- web project https://github.com/Danielyan86/Django-Polls
  - pip install djangorestframework
  - git checkout restapiexample
  - python manage.py migrate
  - python manage.py runserver
  - 127.0.0.1:8000

# 练习

## 分别使用 curl，httpie, 完成基本 API 测试

- curl 请求

  - curl i -X GET "http://127.0.0.1:8000/" (需要在 django setting 注释配置'rest_framework.permissions.IsAuthenticated',，)
  - curl -X POST http://localhost:8000/get_auth_token/ --data "username=admin&password=123456"
  - curl -X GET http://127.0.0.1:8000/users/ -H 'Authorization: Token af60bd228881ea4e2fca375221f39627578026ff'

- httpie 请求
  - http http://127.0.0.1:8000
  - http http://localhost:8000/get_auth_token/ username=admin password=123456

## postman 练习

- 使用 post 发起 get， post 等请求
- 设置环境变量
- 添加自动化用例
- 转化自动化测试代码
- 使用 Newman 客户端执行 collection

## python 自动化练习

- 使用 python requests 包发起 get， post 等请求
- 使用 python unit 对结果进行验证
- requests 文档 https://requests.readthedocs.io/en/master/
