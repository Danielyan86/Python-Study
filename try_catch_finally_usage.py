try:
	A = "this is A"
	A
	print A
except Exception, e:  # except KW just catch the error with Exception class, won't end the program
	print "this is an Exception caught by python:", e
else:
	print "Enter else branch"
	raise AssertionError("this was the end")
finally:
	print "Enter finally phase"
print "----------------------------------------------------------------"

#python interpreter error will all be included in Exception class
try:
	B=2
	print B
except Exception, e:
	print "this is an Exception caught by python:", e
	#Raise function will end this program
	raise AssertionError(e)
	print "this won't be shown on screen if the Exception happened"
else:
	print "Enter else branch"
finally:
	print "Enter finally phase"
print "this won't be shown on screen if the Exception happened"
print "----------------------------------------------------------------"

#this was an example to show how to trigger an exception human
C=False
if C:
	print True
else:
	raise AssertionError("this exception was triggered by human")