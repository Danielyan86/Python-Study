import re,zipfile
Res = re.compile(r'Next nothing is (\d*)')
#create ZipFile
file = zipfile.ZipFile("channel.zip","r")
name_list = file.namelist()
ans = []#list   append
prefix = 90052
suffix = ".txt"
while True:
    try:
        prefix = Res.search(file.read(str(prefix) + suffix)).group(1)
    except:
        print(file.read(str(prefix) + suffix))
        break
    ans.append(file.getinfo(str(prefix) + suffix).comment)
print("".join(ans))