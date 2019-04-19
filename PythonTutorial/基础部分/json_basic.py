import json
import requests

data = [1, 2, 3]
# 将python数据格式转换为json编码字符串
print(json.dumps(data))
# 将python数据格式转换为json编码字符串，并写入文件
with open("data.json", "w+") as f:
    json.dump(data, f)

# 读jaso格式文件，并转化python数据结构
with open("data.json", "r") as f:
    python_data = json.load(f)
    print(python_data)
