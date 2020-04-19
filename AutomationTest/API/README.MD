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
    - git checkout restapiexample
    - python manage.py migrate
    - python manage.py runserver
    - 127.0.0.1:8000

# 练习
## 分别使用curl，httpie, 完成基本API测试
- curl 请求
    - curl i  -X GET "http://127.0.0.1:8000/"  
    - curl curl -X POST http://localhost:8000/get_auth_token/ --data "username=admin&password=123456"
    - curl -X GET http://127.0.0.1:8000/users/ -H 'Authorization: Token af60bd228881ea4e2fca375221f39627578026ff'

- httpie 请求
    - http http://127.0.0.1:8000
    - http http://localhost:8000/get_auth_token/ username=admin password=123456
## postman 练习
- 使用post发起get， post等请求
- 设置环境变量
- 添加自动化用例
- 转化自动化测试代码
- 使用Newman客户端执行collection

## python自动化练习
- 使用python requests 包发起get， post等请求
- 使用python unit 对结果进行验证
