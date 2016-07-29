#!/usr/bin/python

import os
import glob
import sys
import time
import sys
from os.path import dirname
import re
import xml.dom
import xml.dom.minidom
from Constants import *
from testxml import *

search_dir = r"C:\Users"
os.chdir(search_dir)
files = [ file for file in glob.glob(search_dir + "\\" + "*") if os.path.isfile(file)]
files.sort(key=lambda x: os.path.getmtime(x), reverse=True)

#print files[0], os.path.getmtime(files[0])

lastUpdatedFile = files[0]
#print lastUpdatedFile

fileStream = open(lastUpdatedFile, 'r')
cnt = 0
for line in fileStream:
	cnt += 1

print cnt




