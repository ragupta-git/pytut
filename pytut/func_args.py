def argfunc(*args):
    for arg in args:
        print arg


#argfunc(1,2,3,5,4,"rahul")
#l = [1,2,3,54,"rahul"]
#argfunc(l)
#argfunc(*l)


def kw_func(**kwargs):
    for item in kwargs.items():
        print item

#kw_func(x=456, y=3)

def func(*args, **kwargs):
    print args
    for arg in args:
        print arg
    for item in kwargs.items():
        print item

d={"x":456, "y":3}

#func(x=456,y=3)
#func(d)
#func(**d)
func(*d)

