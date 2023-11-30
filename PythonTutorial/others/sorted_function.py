from operator import itemgetter, attrgetter

li = "hello Python, life AdD AdC Ade ADD DDdD Add Okk Eii short!".split()
print(li)
ret = sorted(li)
print(ret)
ret1 = sorted(li, key=lambda x: x[0])
print(ret1)

# Sorting Basics
a_list = [5, 2, 3, 1, 4]
print(sorted(a_list))

b_dic = {1: "D", 2: "B", 3: "B", 4: "E", 5: "A"}
print(sorted(b_dic))

# Key Functions
student_tuples = [
    ("john", "A", 15),
    ("jane", "B", 12),
    ("dave", "B", 10),
]
res = sorted(student_tuples, key=lambda student: student[2])  # sort by age
print(res)

res = sorted("This is a test string from Andrew".split(), key=str.lower)
print(res)

print(sorted(student_tuples, key=itemgetter(2)))
