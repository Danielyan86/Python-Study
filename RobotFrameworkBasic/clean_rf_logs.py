import os
import re

print(os.listdir("."))

pattern = re.compile(r"(.*\.html|.*\.xml)")
for file in os.listdir("."):
    res = pattern.search(file)
    if res:
        print(res.group())

    os.system("rm {0}".format(file))
