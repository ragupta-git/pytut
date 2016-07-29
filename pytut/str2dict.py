#!/usr/bin/python

def convertStrToDict(str):
	str1=str.strip('{}')
	mydict={}
	for every in str1.split(','):
		every.strip()
		z=every.split(':')
		z1=[]
		for every in z:
			every.strip()
			z1.append(every)
		for k in z1:
			mydict[z1[0]]=z1[1]
	return mydict

s="{fdd:1 , gdd:2 }"
print convertStrToDict(s)
