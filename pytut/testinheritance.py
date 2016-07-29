class A(object):
    # Constant
    A_CONST = "A_CONST"
    
    # constructor
    def __init__(self):
        self.public_class_id = "a_public_class_id"
        self._protected_class_id = "a_protected_class_id"
        self.__private_class_id = "a_private_class_id"
        print self.protected_class_id
        
    @property
    def protected_class_id(self):
        return self._protected_class_id
    
        
class B(A):
    def __init__(self):
        self._protected_class_id = "b_protected_class_id"
        super(B,self).__init__()
        #print self.public_class_id
        print self.protected_class_id



def test_set_class_public_variable_using_class():
    print A.A_CONST
    temp = A.A_CONST
    A.A_CONST = "B_CONST"
    print A.A_CONST
    A.A_CONST = temp
    
def test_set_class_public_variable_using_instance():
    a = A()
    print a.A_CONST
    temp = a.A_CONST
    a.A_CONST = "B_CONST"
    print a.A_CONST
    b=A()
    print b.A_CONST
    b.A_CONST = temp
    print A.A_CONST
    print a.A_CONST
    print b.A_CONST
    
def test_protected_variable():
    a1=A()
    print a1.__dict__
    print a1.public_class_id
    print a1.protected_class_id
    #print a1.__private_class_id
    print
    
    b1=B()
    print b1.__dict__
    #print b1.public_class_id
    print b1.protected_class_id
    #print b1.__private_class_id
    b1.new_class_id = "new_class_id"
    print b1.__dict__
    print
    
#    a2=A()
#    print a2.public_class_id
#    print a2._protected_class_id
#    print a2.__dict__
#    print
    
    
if __name__ == '__main__':
    try:
        #print A.A_CONST                     # can be accessed as public using class
        #print A.init_local_variable         # class has no attribute init_local_variable
        #A.access_instance_method_by_class() # public instance method cannot be called directly with class name.
        #a = A()
        #a.access_instance_method_by_object() # public instance method accessible by instance. 
        #print a.A_CONST                      # can be accesses as public using object
        #a.init_local_variable               # object has not attribute init_local_variable
        
        #test_set_class_public_variable_using_class()
        #test_set_class_public_variable_using_instance()
        
        test_protected_variable()
        
        
        
    except Exception, err:
        print "Exception:", str(err)
        import traceback, sys
        print '-'*60
        traceback.print_exc(file=sys.stdout)
        print '-'*60
        
    