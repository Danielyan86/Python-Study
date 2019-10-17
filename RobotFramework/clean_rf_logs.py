import os
import re

print(os.walk("."))

pattern = re.compile(r"(.*\.html|.*\.xml)|.*\.png")
for root, dirs, file_list in os.walk("."):
    # print(root, dirs, file_list)
    for file in file_list:
        path = os.path.join(root, file)
        res = pattern.search(path)
        if res:
            print(res.group())
            os.system("rm {0}".format(path))
