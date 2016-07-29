#!/usr/bin/python
a = ["1","2","3"]
b = ["3",a]
c = ["4",b]

def ListChild(c):
	for i in c:
		print i
		#sleep 10
		if IsChild(i):
			print "True"
			return True
	print "False"
	return False


def IsChild(x):
	return ListChild(x)

ListChild(c)







