# image 镜像练习
- 安装docker到本地环境
- Docker pull ubuntu:16.04  #从官方下载ubuntu镜像到本地
- 查看本地镜像文件
- 删除镜像

# 容器练习
- 启动容器
- 查看容器
- 命令行交互方式进入容器
- 停止一个容器
- 删除一个容器

# DOCKERFILE 练习
- Docker build -t web-app:latest .   #根据当前文件夹下面的dockerfile创建镜像文件
- 查看编译好的image
- Docker run -p 4000:80 web-app      #运行镜像文件并映射端口
- Docker ps                                   #查看正在运行的容器
- 127.0.0.1:4000                          #从外部访问容器里面Web APP

# 数据卷练习
- docker run --rm -p 5904:25900 --name automation-container -v "$(pwd)":/home/seluser/automation automationtest:latest  映射本地磁盘到容器

# 推送练习
- https://cloud.docker.com 注册账号
- Docker login/logout 登录/退出

# 自动化测试综合练习
- 编译自己的自动化镜像文件
- 启动有UI环境的镜像文件
- 编写一个简单的自动化脚本
- 在容器里面跑一个自动化脚本
- 通过selenium grid 方法在容器里面运行脚本
- 启动多个容器，并行运行UI自动化脚本

# docker-compose练习
- 练习docker-compose命令
