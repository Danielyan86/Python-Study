#!/usr/bin/env bash
# 脚本是在dockerfile里面通过add加进去的，所以执行路径应该和dockerfile添加路径一致
docker exec -i automation-container python /home/seluser/automation/myScript/bing_test.py