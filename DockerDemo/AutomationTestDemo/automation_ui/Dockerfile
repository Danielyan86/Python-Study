FROM elgalu/selenium
RUN sudo apt-get update -y \
&& sudo -H pip install selenium \
&& mkdir /home/seluser/automation/
#ADD . /home/seluser/automation/myScript
#切换回工作目录,初次启动容器此文件会在工作目录生成一些相关配置文件，避免和自己的脚本文件混合在一起
WORKDIR /home/seluser/