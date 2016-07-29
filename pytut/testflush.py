#!/usr/bin/python

import sys
from time import sleep

t=0
print "start"
while t<10:
	sys.stdout.write("rahul")
	sys.stdout.flush()
	sleep(2)
	t=t+1

print "over"