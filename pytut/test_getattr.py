
class xyz(object):
	def __init__(self,a,b):
		self._a = 5 
		self._b = 6


class abc(xyz):
	def __init__(self,c,d):
		self._a = c
		self._d = d
		xyz.__init__(self, self.__a,self.__d)
		
	@property
	def a(self):
		return self._a
	
#	@a.setter
#	def a(self, a):
#		self._a = a
		
	def get_attr(self, key):
		return "hello abc_getattr"
		
	def __getattr__(self, key):
		return self.get_attr(key)
	
	def setattr(self, key, value):
		print "setattr"
		self.__dict__[key] = value
	
#	def __setattr__(self,key,value):
#		print "inside setattr"
#		self.__dict__[key] = value

	
#	def __getattribute__(self, attr):
#		return "Hello abc_getattribute"
	
if __name__ == "__main__":
	x = abc(3,4)
	a="a"
	
	print x.__dict__
	
	x.a = 7
	
	print x.__dict__
	
	
#	print x.a
#	print x.b
#	print x.c
#	print "===="
#	print getattr(x,"a")
#	print getattr(x,"b")
#	print getattr(x,"c")
#	print "===="
#	print x.get_attr("a")
#	print x.get_attr("b")
#	print x.get_attr("c")
#	print "===="
#	x.a = 5
#	print x.a
#	print x.c
	
	
