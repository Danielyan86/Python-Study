def counter(start_at=0):
	print "enter counter"
	count = [start_at]
	def incr():
		count[0] += 1
		return count[0]
	return incr


print counter(1)
print counter()()
print counter()()