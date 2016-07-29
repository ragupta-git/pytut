import re
import fileinput

try:
	for line in fileinput.input('test.txt', inplace=1):
		if re.search(r'^\s*</resources>\s*$', line):
			print '    <property name="testtext" value="true"/>'
		print line,
	
except:
	fileinput.close()
	