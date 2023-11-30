import pandas as pd

data = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6], "c": [7, 8, 9]})
print(data)
print("=" * 101)
columns = set(data.columns)
print(columns)
ex_columns = {"c"}
print(ex_columns)
print(list(columns - ex_columns))
#
# # 取单列
# print(f"get cloumn 'a' {data['a']}")
#
print("取多列")
print(data[[]])
#
# # 按标签提取
# print("==")
# print(data.loc[:, 'a'])

df = pd.read_csv("watermelon.csv")
# 查看数据

df.head(3)
df.info()
