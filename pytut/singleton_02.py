def singleton(my_class):
    instances = {}
    print instances
    print my_class
    def get_instance():
        if my_class not in instances:
            instances[my_class] = my_class()
        return instances[my_class]
    return get_instance

@singleton
class TestClass(object):
    pass

print TestClass
#print singleton
#print singleton(TestClass)()

a = TestClass()
print a
b= TestClass()
print b

