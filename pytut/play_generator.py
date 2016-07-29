__author__ = 'ragupta4'

def twice(x):
    return x*2

li = [1,2,3,4,5]
ge = (twice(i) for i in li)

print type(ge)
for i in ge:
    print i