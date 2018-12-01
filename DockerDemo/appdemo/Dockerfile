# Use an official Python runtime as a parent image
#基础镜像
FROM python:3.6-slim

# Set the working directory to /app
# 设置工作目录
WORKDIR /app

# Copy the current directory contents into the container at /app
# 复制当前目录内容到容器里面app目录下面
ADD . /app

# Install any needed packages specified in requirements.txt
# 安装依赖包
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 80 available to the world outside this container
# 暴露容器里面端口到宿主机
EXPOSE 80

# Define environment variable
# 定义环境变量
ENV NAME World

# Run app.py when the container launches
# 容器运行时候执行CMD里面命令
CMD ["python", "app.py"]