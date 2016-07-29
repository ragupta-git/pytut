__author__ = 'ragupta4'

import pyparsing as pp

def func():
    print "hiiii"

# x = pp.Word(pp.alphanums).setResultsName("xr").setParseAction(func)
# print x
# print x.parseString("ddd")["xr"]

class A:
    def __init__(self):
        pass

    def z(self):
        print "z"

    def x(self):
        print "x"

a = A()
a.x().z()
