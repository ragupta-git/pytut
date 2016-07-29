def outside(x=5):
    def inside():
        print x
        print "inside"
    return inside

#print outside
#print outside(x=8)
#outside(x=9)()



def add_one(my_func):
    def add_one_inside():
        return my_func() + 1
    return add_one_inside

def old_func():
    return 3


#print add_one
#print add_one(old_func)
#print add_one(old_func)()

# overriding old function i.e. decorating old function
#old_func = add_one(old_func)
#print old_func()

@add_one
def decorated_old_func():
    return 3

# nothing but add_one(decorated_old_func)()
#print decorated_old_func()


def d_add_one(my_func):
    def d_add_one_inside(*args, **kwargs):
        return my_func(*args, **kwargs) + 1
    return d_add_one_inside

@add_one
def d_decorated_old_func(x=5):
    return x

print d_add_one
print d_decorated_old_func
print d_decorated_old_func()
print d_add_one(d_decorated_old_func)()
#print d_add_one(d_decorated_old_func)(3)

