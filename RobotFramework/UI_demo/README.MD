# 运行demo步骤
## 启动被测试环境
- docker run  -p 8080:8080 oscarcommerce/django-oscar-sandbox
- 打开web注册账号 http://127.0.0.1:8080/en-gb/accounts/login/
- 运行RF脚本
  - robot UI_demo.robot
- 查看日志