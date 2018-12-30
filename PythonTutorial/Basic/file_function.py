import os

try:
    # 创建文件夹
    os.mkdir("new_folder")
except FileExistsError as e:
    print("file is existing")

# 获取当前目录
print("print current folder path:{0}".format(os.getcwd()))
print(os.listdir("."))

# 切换到子目录
os.chdir("./new_folder")
os.chdir("..")
print(os.getcwd())
os.rmdir("new_folder")
