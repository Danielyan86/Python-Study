# join string
print("=" * 20)
a = "123"
b = "456"
print(a + b)

print("".join([a, b]))

print(",".join([a, b]))

# enumerate
print("=" * 20)
a = "string"
for i, j in enumerate(a):
    print(i, j)

# zip()
print("=" * 20)
s, t = "123", "abc"
print(list(zip(s, t)))

# split string
print("=" * 20)
a = "1,2,3,4,5"
print(a.split(","))

# replace
a = "ababababa"
c = a.replace("a", "c")
print(c)
