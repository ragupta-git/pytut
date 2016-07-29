
#!/usr/bin/python

# Import built-in module math
class Employee:
   'Common base class for all employees'
   empCount = 0

   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1
   
   def displayCount(self):
     print "Total Employee %d" % Employee.empCount

   def displayEmployee(self):
      print "Name : ", self.name,  ", Salary: ", self.salary

"This would create first object of Employee class"
emp1 = Employee("Zara", 2000)
"This would create second object of Employee class"
emp2 = Employee("Manni", 5000)
emp1.displayEmployee()
emp2.displayEmployee()
print "Total Employee %d" % Employee.empCount

print "Employee.__doc__:", Employee.__doc__
print "Employee.__name__:", Employee.__name__
print "Employee.__module__:", Employee.__module__
print "Employee.__bases__:", Employee.__bases__
print "Employee.__dict__:", Employee.__dict__

def fixed_writexml(self, writer, indent="", addindent="", newl=""):
	# indent = current indentation
	# addindent = indentation to add to higher levels
	# newl = newline string
	writer.write(indent+"<" + self.tagName)

	attrs = self._get_attributes()
	a_names = attrs.keys()
	a_names.sort()

	for a_name in a_names:
		writer.write(" %s=\"" % a_name)
		xml.dom.minidom._write_data(writer, attrs[a_name].value)
		writer.write("\"")
	if self.childNodes:
		if len(self.childNodes) == 1 \
		  and self.childNodes[0].nodeType == xml.dom.minidom.Node.TEXT_NODE:
			writer.write(">")
			self.childNodes[0].writexml(writer, "", "", "")
			writer.write("</%s>%s" % (self.tagName, newl))
			return
		writer.write(">%s"%(newl))
		for node in self.childNodes:
			node.writexml(writer,indent+addindent,addindent,newl)
		writer.write("%s</%s>%s" % (indent,self.tagName,newl))
	else:
		writer.write("/>%s"%(newl))


