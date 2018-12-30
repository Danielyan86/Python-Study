import os

try:
    # 创建文件夹
    os.mkdir("new_folder")
except FileExistsError as e:
    print(e)
    print("file is existing")

# 获取当前目录
print("=" * 20)
print("print current folder path:{0}".format(os.getcwd()))
# 获取指定目录文件列表

os.listdir(".")
print("list the files:{0}".format(os.listdir(".")))

# 切换到子目录
os.chdir("./new_folder")
os.chdir("..")
print(os.getcwd())
os.rmdir("new_folder")
