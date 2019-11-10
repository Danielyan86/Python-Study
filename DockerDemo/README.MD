# 环境安装和镜像准备
## docker 相关安装
- 推荐学习文档 https://yeasy.gitbooks.io/docker_practice/
- 官网安装文档 https://docs.docker.com/install/
- 中文安装文档 https://yeasy.gitbooks.io/docker_practice/content/install/ 
- docker-compose 安装文档 https://docs.docker.com/compose/install/
- Win10用户需要使用使用正版旗舰版。并开启hyper-V服务和BIOS虚拟化设置。https://jingyan.baidu.com/article/ac6a9a5e1f164a2b653eac33.html
- Docker 安装包建议从官网下载免费社区版
- 无法直接安装在本机的同学，比如win7。可以尝试使用virtualbox安装Ubuntu虚拟机，在虚拟机里面再安装docker。也可以上网搜索其他方式。建议直接安装在本机上。
- 把docker安装在windows的virtualbox里面的，本地访问*IP为192.168.99.100
## 镜像准备
- 安装好docker的同学，请提前拉取一下镜像到本地。如果速度慢，可以配置阿里云或者网易云镜像加速器。
  - Docker pull ubuntu:16.04
  - Docker pull elgalu/selenium
  - docker pull oscarcommerce/django-oscar-sandbox
  
## 其他工具
- VNC客户端安装

# image 镜像练习
- 从官方下载ubuntu镜像到本地
- 查看本地镜像文件
- 删除镜像
- 给存在镜像文件打tag

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
- Docker ps                          #查看正在运行的容器
- 127.0.0.1:4000                     #从外部访问容器里面Web APP

# 数据卷练习
- 练习挂载数据卷到容器
- docker run --rm -p 5904:25900 --name automation-container -v "$(pwd)":/home/seluser/automation automationtest:latest  #映射本地磁盘到容器

# 仓库练习
- https://cloud.docker.com 注册账号
- Docker login/logout 登录/退出
- 推送本地镜像到远程仓库

# 自动化测试综合练习
- 编译自己的自动化镜像文件
- 启动有UI环境的镜像文件
- 编写一个简单的自动化脚本
- 在容器里面跑一个自动化脚本
- 通过selenium grid 方法在容器里面运行脚本
- 启动多个容器，并行运行UI自动化脚本

# docker-compose练习
- 安装和查看docker-compose版本
- 运行示例中的docker-compose文件启动容器
- 在有测试环境的容器中运行自动化测试脚本

# 思考
- docker有些什么样使用场景？
- 结合学过的一些内容，创建自己所需要的镜像文件，比如创建一个