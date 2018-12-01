FROM elgalu/selenium
RUN sudo apt-get update -y \
&& sudo -H pip install selenium \
&& mkdir /home/seluser/automation/
ADD . /home/seluser/automation/myScript
#定义工作目录,初次启动容器此文件会生成一些相关配置文件
WORKDIR /home/seluser/