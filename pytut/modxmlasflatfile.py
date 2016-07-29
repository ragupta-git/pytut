import fileinput
import re

m_file = r"C:\Users\m.txt"
mlist = open(mo_file,'r').readlines()

mlist = map(lambda s: s.strip(), mlist)
print mlist

xml_file = r"gen.xml"

for line in fileinput.input(xml_file, inplace=1):
    mat = re.match(r'^.*<type name="(.*?)".*$', line)
    if mat:
        m = mat.groups()[0]
        if m in mlist:
            line = line.strip()
            line = '<!-- ' + line + ' -->\n'
    print line,
