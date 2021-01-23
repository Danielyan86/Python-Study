import os
import re

path = os.path.abspath(__file__)
current_fir_dir = os.path.dirname(path)
print(current_fir_dir)
print(os.walk(current_fir_dir))

pattern = re.compile(r"(.*\.html|.*\.xml)|.*\.png")
for root, dirs, file_list in os.walk(current_fir_dir):
    # print(root, dirs, file_list)
    for file in file_list:
        path = os.path.join(root, file)
        res = pattern.search(path)
        if res:
            print(res.group())
            os.system("rm {0}".format(path))
