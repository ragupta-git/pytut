__author__ = 'ragupta4'


class Ra(object):
    class _ClassContainer(object):
        def __init__(self):
            self._childClass = None

            # Key is the tuple of naming props and value is the child Ra
            self._childObjects = {}

        def __getitem__(self, key):
            return self._childObjects[key]

        def __contains__(self, key):
            return key in self._childObjects

        def __setitem__(self, key, value):
            self._childObjects[key] = value

        def __delitem__(self, key):
            del self._childObjects[key]

        def __len__(self):
            return len(self._childObjects)

        def __iter__(self):
            return iter(self._childObjects.values())

        def _checkKey(self, key):
            if key not in self._childObjects:
                raise AttributeError

    def __init__(self, class_id):
        self.class_id = class_id
        self.children = self._ClassContainer()

    def add_child(self, Ra):
        self.children[self.class_id] = Ra

    def __getattr__(self, prop):
        return self.children[prop]


class BaseClass(object):
    class _ChildContainer(object):
        class _ClassContainer(object):
            def __init__(self, childClass):
                self._childClass = childClass

                # Key is the tuple of naming props and value is the child Ra
                self._childObjects = {}

            def __getitem__(self, key):
                return self._childObjects[key]

            def __contains__(self, key):
                return key in self._childObjects

            def __setitem__(self, key, value):
                # self._checkKey(key, value)
                self._childObjects[key] = value

            def __delitem__(self, key):
                del self._childObjects[key]

            def __len__(self):
                return len(self._childObjects)

            def __iter__(self):
                return iter(self._childObjects.values())

        class _ChildIter(object):
            def __init__(self, classContainers):
                self._containers = iter(classContainers.values())
                self._currentContainer = None

            def next(self):
                if self._currentContainer is None:
                    # If no Rare containers this statement will throw an
                    # StopIteration exception and we exit eCCe we Rave on
                    # to the next container
                    self._currentContainer = iter(self._containers.next())
                try:
                    return self._currentContainer.next()
                except StopIteration:
                    # Current container is done, see if we have anything eCCe
                    self._currentContainer = None
                    return self.next()

            def __iter__(self):
                return self

        def __init__(self):
            self._classContainers = {}

        def __iter__(self):
            return BaseClass._ChildContainer._ChildIter(self._classContainers)

        def __len__(self):
            numChildren = 0
            for classContainer in self._classContainers:
                numChildren += len(classContainer)
            return numChildren

        def _addChildContainer(self, child_class_id):
            classContainer = self._classContainers.get(child_class_id, None)
            if classContainer is None:
                classContainer = BaseClass._ChildContainer._ClassContainer(child_class_id)
                self._classContainers[child_class_id] = classContainer

            return classContainer

        def _getChildContainer(self, child_class_id):
            classContainer = self._classContainers.get(child_class_id, None)
            return classContainer

    def __init__(self):
        self._class_id = "CC"
        self.__children = BaseClass._ChildContainer()

    @property
    def _children(self):
        return iter(self.__children)

    def __getattr__(self, attrName):
        # We got this call because properties did not match, so look for
        # child class containers
        return self.__children._getChildContainer(attrName)

    def __RadifyChild(self, childRa):
        childContainer = self.__children._addChildContainer(childRa._class_id)
        childContainer[childRa.rn] = childRa

    def add_child(self, Ra):
        self.__RadifyChild(Ra)



class MyClass(BaseClass):
    def __init__(self, rn):
        self.rn = rn
        BaseClass.__init__(self)

# bRa = BaseClass()
# print bRa._c

MyClass = MyClass("MyClass")
print MyClass["CC-MyClass"]




MyClass1 = MyClass("MyClass1")
MyClass.add_child(MyClass1)
print
print list(MyClass.CC)
print list(MyClass._children)

# MyClass2 = MyClass("MyClass2")
# MyClass.add_child(MyClass2)
# print MyClass, MyClass1, MyClass2
# print
# print list(MyClass.CC)
# print MyClass.CC["MyClass1"]
# print MyClass.CC["MyClass2"]
#
# for MyClass in MyClass.CC:
#     print MyClass
#
# print MyClass._children



# class_container = BaseClass._ChildContainer._ClassContainer(MyClass)
# child_cont = BaseClass._ChildContainer("CC")
# child_cont._classContainers["CC"] = class_container

# print class_container
# print child_cont

# MyClass = MyClass()
# print MyClass
# MyClass_1 = MyClass()
# print MyClass_1
# MyClass_2 = MyClass()
# print MyClass_2
#
# MyClass.add_child(MyClass_1)
# MyClass.add_child(MyClass_2)
#
# # MyClass_1_1 = MyClass()
# # MyClass_1.add_child(MyClass_1_1)
#
# print MyClass.__dict__
# print
# # print MyClass.a
# print MyClass.CC

# for CC in MyClass.CC:
#     print CC
