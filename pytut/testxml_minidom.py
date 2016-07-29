#!/usr/bin/python

import xml.dom.minidom

document = """\
<slideshow>
<title>Demo slideshow</title>
<slide><title>Slide title</title>
<point>This is a demo</point>
<point>Of a program for processing slides</point>
</slide>

<slide><title>Another demo slide</title>
<point>It is important</point>
<point>To have more than</point>
<point>one slide</point>
</slide>
</slideshow>
"""

dom = xml.dom.minidom.parseString(document)

#print dom.__dict__
print dom
print dom.documentElement
print dom.documentElement.getElementsByTagName('title')[0]
print dom.documentElement.getElementsByTagName('title')[0].childNodes[0].data
print dom.documentElement.getElementsByTagName('title')[1].childNodes[0].data

if len(dom.documentElement.getElementsByTagName('titles')) == 0:
	print "Titles not Exist"

 
