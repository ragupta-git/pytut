__author__ = 'ragupta4'


class parent(object):
    def __init__(self):
        self.a = "a"

    def _prot(self):
        print "I am prot parent"

    def __priv(self):
        print "I am priv parent"


class child(parent):
    def __init__(self):
        self.b = "b"


c = child()
# c._prot()

# c.__priv()
c._parent__priv()

